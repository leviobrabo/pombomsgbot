import pytest
import asyncio
import sys
from unittest.mock import AsyncMock, MagicMock, patch


def make_tg_user(uid=1, username='user', lang='pt'):
    u = MagicMock()
    u.id = uid
    u.username = username
    u.first_name = 'Test'
    u.last_name = None
    u.language_code = lang
    u.full_name = 'Test User'
    return u


def make_message(chat_type='private', text='/start', uid=1, lang='pt'):
    msg = MagicMock()
    msg.chat.type = chat_type
    msg.chat.id = uid
    msg.text = text
    msg.from_user = make_tg_user(uid=uid, lang=lang)
    msg.content_type = 'text'
    msg.reply_to_message = None
    return msg


# ---------------------------------------------------------------------------
# send_message_broadcast — flood control uses asyncio.sleep (not time.sleep)
# ---------------------------------------------------------------------------

class TestBroadcastFloodControl:
    def test_uses_asyncio_sleep_not_time_sleep(self):
        source = open('pombo.py', encoding='utf-8').read()
        fn_start = source.index('async def send_message_broadcast')
        fn_end = source.index('\nasync def ', fn_start + 1)
        fn_source = source[fn_start:fn_end]
        assert 'await asyncio.sleep' in fn_source
        assert 'time.sleep' not in fn_source

    def test_allowed_updates_excludes_chat_boost(self):
        source = open('pombo.py', encoding='utf-8').read()
        assert 'chat_boost_updated' in source
        assert 'chat_boost_removed' in source
        assert '_broken_update_types' in source


# ---------------------------------------------------------------------------
# Handler tests — pombo imported with scheduler mocked to avoid event loop issue
# ---------------------------------------------------------------------------

@pytest.fixture(scope='module')
def pombo_module():
    import importlib.util

    mock_scheduler = MagicMock()
    mock_scheduler.start = MagicMock()
    mock_scheduler.add_job = MagicMock(return_value=None)

    with patch('apscheduler.schedulers.asyncio.AsyncIOScheduler') as mock_cls:
        mock_cls.return_value = mock_scheduler
        spec = importlib.util.spec_from_file_location('pombo_main', 'pombo.py')
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod


class TestInlineQueryHideBanned:
    def test_banned_user_returns_early(self, pombo_module):
        from pombo.database.models import User

        banned_user = MagicMock()
        banned_user.has_banned = True

        async def run():
            inline_query = MagicMock()
            inline_query.from_user = make_tg_user()
            inline_query.query = 'secret message @alice'

            with patch.object(User, 'get_or_create', return_value=banned_user):
                with patch.object(pombo_module.bot, 'answer_inline_query', new_callable=AsyncMock) as mock_answer:
                    await pombo_module.inline_query_hide(inline_query)
                    mock_answer.assert_not_called()

        asyncio.run(run())


class TestCallbackQueryPostNotFound:
    def test_post_not_found_shows_alert(self, pombo_module):
        from pombo.database.models import Post

        async def run():
            call = MagicMock()
            call.data = '9999 FOR'
            call.from_user = make_tg_user(lang='pt')
            call.message.chat.id = 1
            call.message.id = 1
            call.id = 'cb_id'

            with patch.object(Post, 'get_by_id', side_effect=Exception('not found')):
                with patch.object(pombo_module.bot, 'answer_callback_query', new_callable=AsyncMock) as mock_cb:
                    await pombo_module.callback_query(call)
                    mock_cb.assert_called_once()
                    args, kwargs = mock_cb.call_args
                    assert kwargs.get('show_alert') is True or True in args

        asyncio.run(run())


class TestCmdBanAccessControl:
    def test_non_admin_denied(self, pombo_module):
        from pombo.database.models import User

        async def run():
            msg = make_message(text='/ban 999', uid=9999)
            target = MagicMock()
            target.has_sudo = False

            with patch.object(User, 'get_or_create', return_value=target):
                with patch.object(pombo_module.bot, 'reply_to', new_callable=AsyncMock) as mock_reply:
                    with patch.object(pombo_module, 'admins', []):
                        await pombo_module.cmd_ban(msg)
                        mock_reply.assert_called_once()
                        assert 'negado' in mock_reply.call_args[0][1].lower()

        asyncio.run(run())
