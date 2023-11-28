# Pombo Correio Bot
# Copyright (C) 2023 leviobrabo
#
# This file is a part of < https://github.com/leviobrabo/pombomsgbot/ >
# PLease read the GNU v3.0 License Agreement in
# <https://github.com/leviobrabo/pombomsgbot/blob/main/LICENSE>.

import random

from ..database.models import PostMode
from ..locales.locales_dict import LocalesDict
from telebot import types, util


class QueryResults:
    def __init__(self, locales: LocalesDict):
        self.locales = locales

    def message_too_long(self, lang: str):
        message_content = types.InputTextMessageContent(
            self.locales[lang].too_long_message
        )
        return types.InlineQueryResultArticle(
            id='1',
            title=self.locales[lang].too_long_title,
            input_message_content=message_content,
            description=self.locales[lang].too_long_description,
            thumbnail_url='https://i.imgur.com/xblMvAx.png',
        )

    def mode_for(self, lang: str, post_id, body, scope_string):
        keyboard = types.InlineKeyboardMarkup(
            keyboard=[
                [
                    types.InlineKeyboardButton(
                        self.locales[lang].view,
                        callback_data=str(post_id)
                        + ' '
                        + PostMode.parse_key(PostMode.FOR),
                    )
                ]
            ]
        )
        message_content = types.InputTextMessageContent(
            self.locales[lang].for_message % scope_string
        )
        return types.InlineQueryResultArticle(
            id=str(PostMode.FOR),
            title=self.locales[lang].for_title % scope_string,
            input_message_content=message_content,
            reply_markup=keyboard,
            description=body,
            thumbnail_url='https://i.imgur.com/hHIkDSu.png',
        )

    def mode_except(self, lang: str, post_id, body, scope_string):
        keyboard = types.InlineKeyboardMarkup(
            keyboard=[
                [
                    types.InlineKeyboardButton(
                        self.locales[lang].view,
                        callback_data=str(post_id)
                        + ' '
                        + PostMode.parse_key(PostMode.EXCEPT),
                    )
                ]
            ]
        )
        message_content = types.InputTextMessageContent(
            self.locales[lang].except_message % scope_string
        )
        return types.InlineQueryResultArticle(
            id=str(PostMode.EXCEPT),
            title=self.locales[lang].except_title % scope_string,
            input_message_content=message_content,
            reply_markup=keyboard,
            description=body,
            thumbnail_url='https://i.imgur.com/S6OZMHd.png',
        )

    def mode_spoiler(self, lang: str, post_id, body):
        keyboard = types.InlineKeyboardMarkup(
            keyboard=[
                [
                    types.InlineKeyboardButton(
                        self.locales[lang].view,
                        callback_data=str(post_id)
                        + ' '
                        + PostMode.parse_key(PostMode.SPOILER),
                    )
                ]
            ]
        )
        message_content = types.InputTextMessageContent(
            self.locales[lang].spoiler_message
        )
        return types.InlineQueryResultArticle(
            id=str(PostMode.SPOILER),
            title=self.locales[lang].spoiler_title,
            input_message_content=message_content,
            reply_markup=keyboard,
            description=body,
            thumbnail_url='https://i.imgur.com/mS2ir0T.png',
        )


class Keyboards:
    def __init__(self, locales: LocalesDict):
        self.locales = locales

    def info_keyboard(self, lang: str) -> types.InlineKeyboardMarkup:
        locale = self.locales[lang]
        return types.InlineKeyboardMarkup(
            keyboard=[
                [
                    types.InlineKeyboardButton(
                        locale.button_addGroup,
                        url='https://t.me/pombomsgbot?startgroup=true',
                    )
                ],
                [
                    types.InlineKeyboardButton(
                        locale.button_use_message,
                        url='https://t.me/+0ommac6hJVphMGNh',
                    ),
                    types.InlineKeyboardButton(
                        locale.button_support_message,
                        url='https://t.me/Kylorensbot',
                    ),
                ],
                [
                    types.InlineKeyboardButton(
                        locale.button_channel_message,
                        url='https://t.me/pombomsgbotchannel',
                    ),
                    types.InlineKeyboardButton(
                        locale.button_donate_message,
                        callback_data='donate_button',
                    ),
                ],
                [
                    types.InlineKeyboardButton(
                        locale.button_how_to_use, callback_data='how_to_use'
                    )
                ],
            ]
        )


class Media:
    def group_greeting_sticker_id(self):
        return random.choice(
            (
                'CAACAgEAAxkBAAISQWOC8VsrqyfpWlpii-alLy1_DUbUAAI2AgAC5b2wRNk2tzRjCpEeKwQ',
                'CAACAgEAAxkBAAISQmOC8W08_Xbhp48ieLdp8EYyj27wAAKKAgACK_tIRbbur0yldiPDKwQ',
                'CAACAgEAAxkBAAISQ2OC8Xi3K9ijOfd6S3p0z3rv0Z5SAAIeBQACHJoIRMdNoaZYgx2EKwQ',
            )
        )


class Resources:
    def __init__(self, locales: LocalesDict):
        self.query_results = QueryResults(locales)
        self.keyboards = Keyboards(locales)
        self.media = Media()
