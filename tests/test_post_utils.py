import pytest
from unittest.mock import MagicMock
from pombo.utils.post_utils import (
    PostMode,
    get_formatted_username_or_id,
    get_formatted_username_or_id_chat,
    timeFormatter,
)


def test_timeFormatter_zero():
    assert timeFormatter(0) == '00:00:00'


def test_timeFormatter_minutes():
    assert timeFormatter(90) == '00:01:30'


def test_timeFormatter_hours():
    assert timeFormatter(3661) == '01:01:01'


def test_get_formatted_username_or_id_with_username():
    user = MagicMock()
    user.username = 'testuser'
    assert get_formatted_username_or_id(user) == '@testuser'


def test_get_formatted_username_or_id_without_username():
    from telebot import types
    user = MagicMock(spec=types.User)
    user.username = None
    user.id = 12345
    assert get_formatted_username_or_id(user) == 'id12345'


def test_get_formatted_username_or_id_db_user():
    user = MagicMock(spec=[])
    user.username = None
    user.user_id = 99999
    assert get_formatted_username_or_id(user) == 'id99999'


def test_get_formatted_username_or_id_chat_with_username():
    chat = MagicMock()
    chat.username = 'mygroup'
    assert get_formatted_username_or_id_chat(chat) == '@mygroup'


def test_get_formatted_username_or_id_chat_without_username():
    from telebot import types
    chat = MagicMock(spec=types.Chat)
    chat.username = None
    chat.id = 777
    assert get_formatted_username_or_id_chat(chat) == 'id777'


def test_postmode_values():
    assert PostMode.SPOILER.value == 0
    assert PostMode.FOR.value == 1
    assert PostMode.EXCEPT.value == 2


def test_postmode_parse_key():
    assert PostMode.parse_key(PostMode.SPOILER) == 'SPOILER'
    assert PostMode.parse_key(PostMode.FOR) == 'FOR'
    assert PostMode.parse_key(PostMode.EXCEPT) == 'EXCEPT'
