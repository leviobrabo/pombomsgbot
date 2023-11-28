# Pombo Correio Bot
# Copyright (C) 2023 leviobrabo
#
# This file is a part of < https://github.com/leviobrabo/pombomsgbot/ >
# PLease read the GNU v3.0 License Agreement in
# <https://github.com/leviobrabo/pombomsgbot/blob/main/LICENSE>.


from enum import Enum

from telebot import types, util


class BaseEnum(Enum):
    @staticmethod
    def parse_key(full_name: Enum):
        return str(full_name).split('.')[-1]


class PostMode(BaseEnum):
    SPOILER = 0
    FOR = 1
    EXCEPT = 2


def get_formatted_username_or_id(user):
    user_id = user.id if isinstance(user, types.User) else user.user_id
    return (
        'id' + str(user_id) if user.username is None else '@' + user.username
    )


def get_formatted_username_or_id_chat(chat):
    chat_id = chat.id if isinstance(chat, types.Chat) else chat.chat_id
    return (
        'id' + str(chat_id) if chat.username is None else '@' + chat.username
    )


def timeFormatter(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f'{h:02d}:{m:02d}:{s:02d}'
