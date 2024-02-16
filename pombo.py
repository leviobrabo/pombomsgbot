# Pombo Correio Bot
# Copyright (C) 2023 leviobrabo
#
# This file is a part of < https://github.com/leviobrabo/pombomsgbot/ >
# PLease read the GNU v3.0 License Agreement in
# <https://github.com/leviobrabo/pombomsgbot/blob/main/LICENSE>.

import asyncio
import os
import random
import re
import time
from datetime import datetime
from threading import Thread
from dotenv import load_dotenv

import psutil
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger
from telebot import types, util
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_helper import ApiTelegramException

from pombo.database.models import Group, Post, PostMode, User
from pombo.locales.locales import locales
from pombo.utils.post_utils import get_formatted_username_or_id, timeFormatter
from pombo.utils.resources import Resources

admins = os.environ['ADMINS'].split(',')

logger.add(os.environ['LOG_PATH'])
rsc = Resources(locales)
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


inline_query_regex = re.compile(r'^.+([ \n](@\w+|id[0-9]+))+$')
scope_regex = re.compile(r'([ \n](@\w+|id[0-9]+))+$')

ignored_chat_ids = set()
bot = AsyncTeleBot(os.environ['API_TOKEN'])

scheduler = AsyncIOScheduler()
channelStatusId = int(os.environ['channelStatusId'])

broadcast_text = 'Envie a mensagem que deseja compartilhar com os {}!'



async def set_my_configs():
    for locale in locales.locales:
        try:
            await bot.set_my_commands(
                [
                    types.BotCommand('/start', locales[locale].commands_start),
                    types.BotCommand('/help', locales[locale].commands_help),
                ],
                language_code=locale,
                scope=types.BotCommandScopeAllPrivateChats(),
            )
        except Exception as ex:
            logger.error(ex)
        try:
            await bot.set_my_name(
                name=locales[locale].bot_name, language_code=locale
            )
        except Exception as ex:
            logger.error(ex)
        try:
            await bot.set_my_description(
                description=locales[locale].description, language_code=locale
            )
        except Exception as ex:
            logger.error(ex)
        try:
            await bot.set_my_short_description(
                short_description=locales[locale].short_description,
                language_code=locale,
            )
        except Exception as ex:
            logger.error(ex)
    for admin in admins:
        try:
            await bot.set_my_commands(
                [
                    types.BotCommand('/start', locales['pt'].commands_start),
                    types.BotCommand('/help', locales['pt'].commands_help),
                    types.BotCommand('/sys', 'Uso do servidor'),
                    types.BotCommand('/sudo', 'Elevar usuário'),
                    types.BotCommand('/ban', 'Banir usuário do bot'),
                    types.BotCommand('/sudolist', 'Lista de usuários sudo'),
                    types.BotCommand('/banneds', 'Lista de usuários banidos'),
                    types.BotCommand(
                        '/bcusers', 'Enviar msg broadcast para usuários'
                    ),
                    types.BotCommand(
                        '/bcgps', 'Enviar msg broadcast para grupos'
                    ),
                ],
                scope=types.BotCommandScopeChat(chat_id=admin),
            )
        except Exception as ex:
            logger.error(ex)


async def sendStatus():
    start = datetime.now()
    replied = await bot.send_message(channelStatusId, 'Bot is ON')
    end = datetime.now()
    m_s = (end - start).microseconds // 1000
    uptime = int(time.time() - start_time)
    uptime_formatted = timeFormatter(uptime)
    await bot.edit_message_text(
        f'#Pombomsgbot #Status\n\nStatus: ON\nPing: `{m_s}ms`\nUptime: `{uptime_formatted}`\nUsers: `{count_users()}`\nPrivate message: `{count_post()}`',
        chat_id=replied.chat.id,
        message_id=replied.message_id,
        parse_mode='Markdown',
    )


def timeFormatter(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    hoursFormatted = str(hours).zfill(2)
    minutesFormatted = str(minutes).zfill(2)
    secondsFormatted = str(secs).zfill(2)

    return f'{hoursFormatted}:{minutesFormatted}:{secondsFormatted}'


start_time = time.time()
scheduler.add_job(
    sendStatus,
    'cron',
    hour=12,
    minute=0,
    second=5,
    timezone='America/Sao_Paulo',
)
scheduler.start()


def ignore(chat_id, timeout):
    ignored_chat_ids.add(chat_id)
    time.sleep(timeout)
    ignored_chat_ids.remove(chat_id)


def create_post(author: User, content: str, scope: set = ()):
    try:
        result = Post.create(
            author=author,
            content=content,
            scope=' '.join(scope).replace('@', ''),
            creation_time=datetime.now(),
        )
        logger.info(
            '#'
            + str(result.get_id())
            + ' foi criado por '
            + get_formatted_username_or_id(author)
        )
        return result
    except Exception as e:
        logger.error(
            'nova postagem não pode ser criada por '
            + get_formatted_username_or_id(author)
        )
        logger.error(e)


def count_users():
    return User.select().count()


def count_per_locates():
    all_users = User.select()
    language_code_count = {}
    for user in all_users:
        if language_code_count.get(user.language_code):
            language_code_count[user.language_code] += 1
        else:
            language_code_count[user.language_code] = 1
    return language_code_count


def count_post():
    return Post.select().count()


def count_groups():
    return Group.select().count()


def list_all_users_db():
    return User.select(User.user_id, User.has_dialog)


def list_all_groups_db():
    return Group.select(Group.group_id, Group.has_dialog)


def get_sudo_list():
    return User.select(User.user_id, User.first_name).where(User.has_sudo)


def get_banned_list():
    return User.select(User.user_id, User.first_name).where(User.has_banned)


async def send_new_user_message(user):
    group_id = os.environ['GROUP_ID']
    text = f'#Pombomsgbot #New_user\n\n'
    text += f"<b>User:</b> <a href='tg://user?id={user.id}'>{user.first_name}</a>\n"
    text += f'<b>ID:</b> <code>{user.id}</code>\n'
    text += f"<b>Username:</b> {'@'+user.username if user.username else 'Não informado'}\n"
    text += f'<b>LANG:</b> {user.language_code.upper()}'
    await bot.send_message(chat_id=group_id, text=text, parse_mode='HTML')


async def send_new_group_message(chat):
    if chat.username:
        chatusername = f'@{chat.username}'
    else:
        chatusername = 'Private Group'
    await bot.send_message(
        os.environ['GROUP_ID'],
        text=f'#Pombomsgbot #New_Group\n\n'
        f'<b>Chat:</b> {chat.title}\n'
        f'<b>ID:</b> <code>{chat.id}</code>\n'
        f'<b>Link:</b> {chatusername}',
        parse_mode='html',
        disable_web_page_preview=True,
        message_thread_id=38545,
    )


async def send_message_broadcast(message, receiver):
    target_object = None
    if receiver == 'grupos':
        all_users = list_all_groups_db()
        target_object = Group
    elif receiver == 'users':
        all_users = list_all_users_db()
        target_object = User
    else:
        raise Exception('Tipo inválido!')
    keyboard = None
    statistics = {'actives': 0, 'inactives': 0, 'sucess': 0, 'fail': 0}
    for user in all_users:
        if not user.has_dialog:
            statistics['inactives'] += 1
            continue
        else:
            statistics['actives'] += 1
        retry = 3
        for _try in range(retry):
            try:
                if message.content_type == 'text':
                    await bot.send_message(
                        user,
                        message.text,
                        reply_markup=keyboard,
                        disable_web_page_preview=True,
                    )
                elif message.content_type == 'photo':
                    if message.caption:
                        await bot.send_photo(
                            user,
                            message.photo[-1].file_id,
                            message.caption,
                            reply_markup=keyboard,
                        )
                    else:
                        await bot.send_photo(
                            user,
                            message.photo[-1].file_id,
                            reply_markup=keyboard,
                        )
                elif message.content_type == 'audio':
                    if message.caption:
                        await bot.send_audio(
                            user,
                            message.audio.file_id,
                            caption=message.caption,
                            reply_markup=keyboard,
                        )
                    else:
                        await bot.send_audio(
                            user, message.audio.file_id, reply_markup=keyboard
                        )
                elif message.content_type == 'video':
                    if message.caption:
                        await bot.send_video(
                            user,
                            message.video.file_id,
                            caption=message.caption,
                            reply_markup=keyboard,
                        )
                    else:
                        await bot.send_video(
                            user, message.video.file_id, reply_markup=keyboard
                        )
                elif message.content_type == 'sticker':
                    await bot.send_sticker(
                        user, message.sticker.file_id, reply_markup=keyboard
                    )
                elif message.content_type == 'voice':
                    await bot.send_voice(
                        user, message.voice.file_id, reply_markup=keyboard
                    )
                elif message.content_type == 'video_note':
                    await bot.send_video_note(
                        user, message.video_note.file_id, reply_markup=keyboard
                    )
                elif message.content_type == 'animation':
                    if message.caption:
                        await bot.send_animation(
                            user,
                            message.document.file_id,
                            caption=message.caption,
                            reply_markup=keyboard,
                        )
                    else:
                        await bot.send_animation(
                            user,
                            message.document.file_id,
                            reply_markup=keyboard,
                        )
                statistics['sucess'] += 1
                break
            except ApiTelegramException as ex:
                if ex.error_code == 429:
                    cooldown = ex.result_json['parameters']['retry_after']
                    logger.error(
                        f'erro de Flood, tentativa: {_try} , esperar por:',
                        cooldown,
                    )
                    time.sleep(cooldown + 1)
                    continue
                else:
                    target_object.disable_user(user)
                    statistics['fail'] += 1
                    statistics['inactives'] += 1
                    statistics['actives'] -= 1
                    break
            except Exception as erro:
                logger.error(f'{user} Erro anuncio {erro}')
                statistics['fail'] += 1
                break
        else:
            statistics['fail'] += 1
    return statistics


def runThreadSendMsg(args, target):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_message_broadcast(args, target))
    loop.close()


@bot.inline_handler(
    lambda query: re.match(inline_query_regex, query.query.replace('\n', ' '))
)
async def inline_query_hide(inline_query: types.InlineQuery):
    try:
        target = User.get_or_create(inline_query.from_user)
        
        if target.has_banned:
            return
        target.inline_queries_count += 1
        target.save()

        if target.has_dialog:
            target.save()
        else:
            await send_new_user_message(inline_query.from_user)

        body = scope_regex.sub('', inline_query.query)
        if len(body) > 200:
            await bot.answer_inline_query(
                inline_query.id,
                [rsc.query_results.message_too_long(target.language_code)],
            )
            return

        raw_scope = re.sub(
            r'(id)([0-9]+)', r'\g<2>', inline_query.query[len(body) + 1:]
        ).split(' ')
        marker = set()
        scope = [
            not marker.add(x.casefold()) and x
            for x in raw_scope
            if x.casefold() not in marker
        ]
        post = create_post(target, body, set(scope))

        formatted_scope = ', '.join(scope[:-1])
        if len(scope) > 1:
            formatted_scope += (
                ' %s ' % locales[target.language_code].and_connector
                + scope[-1]
            )
        else:
            formatted_scope = scope[0]

        await bot.answer_inline_query(
            inline_query.id,
            [
                rsc.query_results.mode_for(
                    target.language_code, post.get_id(), body, formatted_scope
                ),
                rsc.query_results.mode_except(
                    target.language_code, post.get_id(), body, formatted_scope
                ),
            ],
            cache_time=0,
        )
    except Exception as e:
        logger.error(e)
        logger.warning(
            'não pode lidar com a consulta inline ocultar de '
            + get_formatted_username_or_id(inline_query.from_user)
            + ' com carga útil: "'
            + inline_query.query
            + '"'
        )


@bot.inline_handler(lambda query: len(query.query) > 0)
async def inline_query_spoiler(inline_query: types.InlineQuery):
    try:
        target = User.get_or_create(inline_query.from_user)
        if target.has_banned:
            await bot.answer_inline_query(
                inline_query.id,
                [],
                switch_pm_text='YOU ARE BANNED!',
                cache_time=0,
                switch_pm_parameter='you_are_banned',
            )
            return
        target.inline_queries_count += 1
        target.save()

        body = inline_query.query
        if len(body) > 200:
            await bot.answer_inline_query(
                inline_query.id,
                [rsc.query_results.message_too_long(target.language_code)],
            )
            return

        post = create_post(target, body)
        await bot.answer_inline_query(
            inline_query.id,
            [
                rsc.query_results.mode_spoiler(
                    target.language_code, post.get_id(), body
                )
            ],
        )
    except Exception as e:
        logger.error(e)
        logger.warning(
            'não pode lidar com spoiler de consulta em linha de '
            + get_formatted_username_or_id(inline_query.from_user)
            + ' com carga útil: "'
            + inline_query.query
            + '"'
        )


@bot.inline_handler(func=lambda m: True)
async def inline_query_help(inline_query: types.InlineQuery):
    try:
        target = User.get_or_create(inline_query.from_user)
        if not target.has_banned:
            await bot.answer_inline_query(
                inline_query.id,
                [],
                switch_pm_text=locales[
                    inline_query.from_user.language_code
                ].how_to_use,
                cache_time=0,
                switch_pm_parameter='how_to_use',
            )

            target.inline_queries_count += 1
            target.save()
        else:
            await bot.answer_inline_query(
                inline_query.id,
                [],
                switch_pm_text='YOU ARE BANNED!',
                cache_time=0,
                switch_pm_parameter='you_are_banned',
            )
    except Exception as e:
        logger.error(e)
        logger.warning(
            'não pode lidar com a ajuda de consulta em linha de '
            + get_formatted_username_or_id(inline_query.from_user)
            + ' com carga útil: "'
            + inline_query.query
            + '"'
        )


@bot.callback_query_handler(func=lambda m: True)
async def callback_query(call: types.CallbackQuery):
    try:
        if call.data == 'donate_button':
            buttons = types.InlineKeyboardMarkup(
                keyboard=[
                    [
                        types.InlineKeyboardButton(
                            locales[call.from_user.language_code].button_back,
                            callback_data='back_to_home',
                        )
                    ]
                ]
            )
            if call.from_user.language_code == 'pt-br':
                text_msg = (
                    f'──❑ 「 {locales[call.from_user.language_code].button_donate_message} 」 ❑──\n\n'
                    ' ☆ <b>Pix:</b>\n <code>32dc79d2-2868-4ef0-a277-2c10725341d4</code>\n\n'
                    ' ☆ <b>BTC:</b>\n <code>bc1qjxzlug0cwnfjrhacy9kkpdzxfj0mcxc079axtl</code>\n\n'
                    ' ☆ <b>ETH/USDT:</b>\n <code>0x1fbde0d2a96869299049f4f6f78fbd789d167d1b</code>'
                )
                await bot.edit_message_text(
                    text_msg,
                    call.message.chat.id,
                    call.message.id,
                    parse_mode='HTML',
                    reply_markup=buttons,
                )
            else:
                text_msg = (
                    f'──❑ 「 {locales[call.from_user.language_code].button_donate_message} 」 ❑──\n\n'
                    ' ☆ <b>BTC:</b>\n <code>bc1qjxzlug0cwnfjrhacy9kkpdzxfj0mcxc079axtl</code>\n\n'
                    ' ☆ <b>ETH/USDT:</b>\n <code>0x1fbde0d2a96869299049f4f6f78fbd789d167d1b</code>'
                )
                await bot.edit_message_text(
                    text_msg,
                    call.message.chat.id,
                    call.message.id,
                    parse_mode='HTML',
                    reply_markup=buttons,
                )
        elif call.data == 'how_to_use':
            buttons = types.InlineKeyboardMarkup(
                keyboard=[
                    [
                        types.InlineKeyboardButton(
                            locales[call.from_user.language_code].button_back,
                            callback_data='back_to_home',
                        )
                    ]
                ]
            )
            await bot.edit_message_text(
                locales[call.from_user.language_code].how_to_use_text,
                call.message.chat.id,
                call.message.id,
                parse_mode='HTML',
                reply_markup=buttons,
            )
        elif call.data == 'back_to_home':
            await bot.edit_message_text(
                locales[call.from_user.language_code].info_message,
                call.message.chat.id,
                call.message.id,
                parse_mode='HTML',
                reply_markup=rsc.keyboards.info_keyboard(
                    lang=call.from_user.language_code
                ),
                disable_web_page_preview=True,
            )
        else:
            (post_id, mode) = str(call.data).split(' ')
            try:
                post = Post.get_by_id(post_id)
            except Exception as e:
                await bot.answer_callback_query(
                    call.id,
                    text=locales[call.from_user.language_code].not_accessible,
                    show_alert=True,
                )
                return

            target = User.get_or_create(call.from_user)
            if post.can_be_accessed_by(call.from_user, PostMode[mode]):
                logger.info(
                    '#'
                    + post_id
                    + ': '
                    + get_formatted_username_or_id(call.from_user)
                    + ' - access granted'
                )
                await bot.answer_callback_query(
                    call.id,
                    post.content.replace(
                        '{username}',
                        get_formatted_username_or_id(call.from_user),
                    )
                    .replace('{uid}', 'id' + str(target.user_id))
                    .replace(
                        '{lang}',
                        'unknown'
                        if target.language_code is None
                        else target.language_code,
                    )
                    .replace('{pid}', '#' + post_id)
                    .replace('{created}', str(post.creation_time))
                    .replace('{queries}', str(target.inline_queries_count))
                    .replace(
                        '{first_interaction}',
                        str(target.first_interaction_time),
                    )
                    .replace('{dialog}', 'Sim' if target.has_dialog else 'Não')
                    .replace('{utc}', str(datetime.utcnow()))
                    .replace('{date}', datetime.utcnow().strftime('%Y-%m-%d'))
                    .replace('{time}', datetime.utcnow().strftime('%H:%M'))
                    .replace('{name}', call.from_user.full_name)
                    .replace('{first_name}', target.first_name)
                    .replace(
                        '{last_name}',
                        '' if target.last_name is None else target.last_name,
                    ),
                    True,
                )
            else:
                logger.info(
                    '#'
                    + post_id
                    + ': '
                    + get_formatted_username_or_id(call.from_user)
                    + ' - access denied'
                )
                await bot.answer_callback_query(
                    call.id,
                    locales[call.from_user.language_code].not_allowed,
                    True,
                )
    except Exception as e:
        logger.error(e)
        logger.warning(
            'não pode lidar com a consulta de retorno de chamada de '
            + get_formatted_username_or_id(call.from_user)
            + ' com carga útil: "'
            + call.data
            + '"'
        )


@bot.message_handler(commands=['stats'])
async def cmd_stats(message: types.Message):
    try:
        user_stats = f' ☆ {count_users()} usuários\n ☆ {count_groups()} Grupos\n ☆ {count_post()} mensagem privadas enviadas'

        lang_stats_title = ' ☆ Estatísticas por Idioma:'
        lang_stats = '\n'.join(
            [
                f' ☆ {lang.upper()} -> {count}'
                for lang, count in count_per_locates().items()
                if lang is not None
            ]
        )

        await bot.reply_to(
            message,
            f'\n──❑ 「 Bot Stats 」 ❑──\n\n{user_stats}\n\n{lang_stats_title}\n\n{lang_stats}',
        )
    except Exception as e:
        logger.error(e)
        logger.warning(
            'Não é possível manipular o comando /stats de '
            + get_formatted_username_or_id(message.from_user)
        )


@bot.message_handler(commands=['sudolist'])
async def cmd_sudolist(message: types.Message):
    if message.chat.type == 'private':
        target = User.get_or_create(message.from_user)
        if str(message.chat.id) in admins or target.has_sudo:
            msg_txt = '──❑ 「 Sudo List 」 ❑──\n\n'
            sudo_list = get_sudo_list()
            for sudoUser in sudo_list:
                msg_txt += f' ☆ {sudoUser.user_id} {sudoUser.first_name}\n'
            try:
                await bot.reply_to(message, msg_txt)
            except Exception as e:
                logger.error(e)
                logger.warning(
                    'Não é possível manipular o comando /stats de '
                    + get_formatted_username_or_id(message.from_user)
                )


@bot.message_handler(commands=['banneds'])
async def cmd_banneds(message: types.Message):
    if message.chat.type == 'private':
        target = User.get_or_create(message.from_user)
        if str(message.chat.id) in admins or target.has_sudo:
            msg_txt = '──❑ 「 Banned List 」 ❑──\n\n'
            banned_list = get_banned_list()
            for bannedUser in banned_list:
                msg_txt += f' ☆ {bannedUser.user_id} {bannedUser.first_name}\n'
            try:
                await bot.reply_to(message, msg_txt)
            except Exception as e:
                logger.error(e)
                logger.warning(
                    'Não é possível manipular o comando /stats de '
                    + get_formatted_username_or_id(message.from_user)
                )


@bot.message_handler(commands=['sys'])
async def cmd_sys(message: types.Message):
    if str(message.chat.id) in admins:
        await bot.reply_to(
            message,
            f'\n──❑ 「 System Stats 」 ❑──\n\n ☆ CPU usage: {psutil.cpu_percent(4)} %\n ☆ RAM usage: {psutil.virtual_memory()[2]} %',
        )


@bot.message_handler(commands=['sudo', 'unsudo'])
async def cmd_sudo(message: types.Message):
    if message.chat.type == 'private':
        if str(message.chat.id) in admins:
            if message.text.startswith('/sudo '):
                user_to_elevate = message.text[message.text.find(' ') + 1:]
                try:
                    user_to_elevate = int(user_to_elevate)
                    User.set_sudo(user_to_elevate)
                except Exception as ex:
                    await bot.reply_to(
                        message, f'Erro: ID de usuário incorreto!'
                    )
                    return
                else:
                    await bot.reply_to(
                        message, f'User {user_to_elevate} now is sudo!'
                    )
            elif message.text.startswith('/unsudo '):
                user_to_unelevate = message.text[message.text.find(' ') + 1:]
                try:
                    user_to_unelevate = int(user_to_unelevate)
                    User.set_sudo(user_to_unelevate, False)
                except Exception as ex:
                    await bot.reply_to(
                        message, f'Erro: ID de usuário incorreto!'
                    )
                    return
                else:
                    await bot.reply_to(
                        message, f'User {user_to_unelevate} now is no sudo!'
                    )
            else:
                await bot.reply_to(
                    message, f'Você deve informar um ID como argumento!'
                )
        else:
            await bot.reply_to(message, f'Acesso negado!')


@bot.message_handler(commands=['ban', 'unban'])
async def cmd_ban(message: types.Message):
    if message.chat.type == 'private':
        target = User.get_or_create(message.from_user)
        if str(message.chat.id) in admins or target.has_sudo:
            if message.text.startswith('/ban '):
                user_to_ban = message.text[message.text.find(' ') + 1:]
                try:
                    user_to_ban = int(user_to_ban)
                    User.set_banned(user_to_ban)
                except Exception as ex:
                    await bot.reply_to(
                        message, f'Erro: ID de usuário incorreto!'
                    )
                    return
                else:
                    await bot.reply_to(
                        message, f'User {user_to_ban} now is banned!'
                    )
            elif message.text.startswith('/unban '):
                user_to_unban = message.text[message.text.find(' ') + 1:]
                try:
                    user_to_unban = int(user_to_unban)
                    User.set_banned(user_to_unban, False)
                except Exception as ex:
                    await bot.reply_to(
                        message, f'Erro: ID de usuário incorreto!'
                    )
                    return
                else:
                    await bot.reply_to(
                        message, f'User {user_to_unban} now is unbanned!'
                    )
            else:
                await bot.reply_to(
                    message, f'Você deve informar um ID como argumento!'
                )
        else:
            await bot.reply_to(message, f'Acesso negado!')


@bot.message_handler(commands=['start', 'help'])
async def cmd_start(message: types.Message):
    if message.chat.type == 'private':
        if message.chat.id in ignored_chat_ids:
            return
        Thread(target=ignore, args=(message.chat.id, 1)).start()

        target = User.get_or_create(message.from_user)
        if target.has_dialog:
            target.save()
        else:
            await send_new_user_message(message.from_user)
        if message.text.startswith('/start '):
            cmd_arg = message.text[7:]
            if cmd_arg == 'how_to_use':
                await bot.reply_to(
                    message,
                    locales[message.from_user.language_code].how_to_use_link,
                )
                return
        await bot.reply_to(
            message,
            text=locales[message.from_user.language_code].info_message,
            parse_mode='html',
            reply_markup=rsc.keyboards.info_keyboard(
                lang=message.from_user.language_code
            ),
            disable_web_page_preview=True,
        )
    else:
        target = Group.get_or_create(message.chat)
        if target.has_dialog:
            target.save()
        else:
            await send_new_group_message(message.chat)


@bot.message_handler(commands=['bcusers', 'bcgps'])
async def cmd_broadcast(message: types.Message):
    if message.chat.type == 'private':
        target = User.get_or_create(message.from_user)
        if str(message.chat.id) in admins or target.has_sudo:
            if message.text.startswith('/bcusers'):
                await bot.send_message(
                    message.chat.id,
                    broadcast_text.format('users'),
                    reply_markup=types.ForceReply(
                        input_field_placeholder='Broadcast users...'
                    ),
                )
            else:
                await bot.send_message(
                    message.chat.id,
                    broadcast_text.format('grupos'),
                    reply_markup=types.ForceReply(
                        input_field_placeholder='Broadcast groups...'
                    ),
                )


# @bot.message_handler(content_types=util.content_type_media)
# async def all_messages(message: types.Message):
#     try:
#         if message.chat.id in ignored_chat_ids:
#             return
#         Thread(target=ignore, args=(message.chat.id, 1)).start()
#         command = None
#         if message.content_type == 'text':
#             if message.text.startswith('/'):
#                 command = message.text
#                 if message.text.find(' ') > 0:
#                     command = message.text[: message.text.find(' ')]
#         if command is not None and command.lower().endswith(
#             (await bot.get_me()).username.lower()
#         ):
#             command = command.split('@')[0]
#         if message.chat.type == 'private':
#             target = User.get_or_create(message.from_user)
#             if target.has_dialog:
#                 target.save()
#             else:
#                 await send_new_user_message(message.from_user)
#         else:
#             target = Group.get_or_create(message.chat)
#             if target.has_dialog:
#                 target.save()
#             else:
#                 await send_new_group_message(message.chat)
#         if message.chat.type == 'private' and str(message.chat.id) in admins:
#             if message.reply_to_message:
#                 if message.reply_to_message.text in [
#                     broadcast_text.format('users'),
#                     broadcast_text.format('grupos'),
#                 ]:
#                     type_permited = [
#                         'text',
#                         'photo',
#                         'audio',
#                         'video',
#                         'sticker',
#                         'voice',
#                         'video_note',
#                         'animation',
#                     ]
#                     if message.content_type in type_permited:
#                         target_type = ''
#                         result_broadcast = {}
#                         if (
#                             message.reply_to_message.text
#                             == broadcast_text.format('users')
#                         ):
#                             target_type = 'users'
#                             result_broadcast = await send_message_broadcast(
#                                 message, 'users'
#                             )
#                         elif (
#                             message.reply_to_message.text
#                             == broadcast_text.format('grupos')
#                         ):
#                             target_type = 'grupos'
#                             result_broadcast = await send_message_broadcast(
#                                 message, 'grupos'
#                             )
#                         else:
#                             return
#                         msg_result = (
#                             f'\n──❑ 「 <b>Broadcast Completed</b> 」 ❑──\n\n ☆ Total {target_type}: {result_broadcast["actives"]+result_broadcast["inactives"]}\n'
#                             f' ☆ Actives: {result_broadcast["actives"]}\n ☆ Inactives: {result_broadcast["inactives"]}\n'
#                             f' ☆ Sucess: {result_broadcast["sucess"]}\n ☆ Fail: {result_broadcast["fail"]}'
#                         )
#                         await bot.send_message(
#                             message.chat.id, msg_result, parse_mode='HTML'
#                         )
#                     else:
#                         await bot.reply_to(message, 'Tipo não permitido')
#                     return
#     except Exception as e:
#         logger.error(e)
#         logger.warning(
#             'não é possível enviar informações para chat_id='
#             + str(message.chat.id)
#         )


@bot.my_chat_member_handler()
async def send_group_greeting(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if message.chat.type != 'private' and new.status in [
        'member',
        'administrator',
    ]:
        try:
            target = Group.get_or_create(message.chat)
            if target.has_dialog:
                target.save()
            else:
                await send_new_group_message(message.chat)
            bot_user = await bot.get_me()
            group_id = message.chat.id
            await bot.send_sticker(
                group_id, rsc.media.group_greeting_sticker_id()
            )
            await bot.send_message(
                group_id,
                text=locales[
                    message.from_user.language_code
                ].group_greeting_message
                % (bot_user.full_name, bot_user.username),
                parse_mode='html',
                disable_web_page_preview=True,
            )
        except Exception as e:
            logger.error(e)


GROUP_ID = os.environ['GROUP_ID']


async def send_initial_message():
    await bot.send_message(
        GROUP_ID,
        '<b>#Pombomsgbot #Online</b>\n\nBot is now playing ...',
        parse_mode='HTML',
        message_thread_id=38545,
    )


async def send_shutdown_message():
    await bot.send_message(
        GROUP_ID,
        '<b>#Pombomsgbot #Offline</b>\n\nBot is now off ...',
        parse_mode='HTML',
        message_thread_id=38545,
    )


if __name__ == '__main__':
    try:
        logger.info('Start polling...')
        asyncio.run(send_initial_message())
        # asyncio.run(set_my_configs())
        asyncio.run(
            bot.infinity_polling(
                allowed_updates=util.update_types, skip_pending=True
            )
        )
    except KeyboardInterrupt:
        logger.info('Bot stopped by the user')
        asyncio.run(send_shutdown_message())
    except Exception as e:
        logger.error(e)
