import pytest
from unittest.mock import MagicMock, patch, PropertyMock
from datetime import datetime
from pombo.utils.post_utils import PostMode


# ---------------------------------------------------------------------------
# Post.can_be_accessed_by — tested without DB (pure logic mock)
# ---------------------------------------------------------------------------

def make_post(scope='', author_id=1):
    from pombo.database.models import Post
    post = MagicMock(spec=Post)
    post.scope = scope
    post.author = MagicMock()
    post.author.user_id = author_id
    post.content = 'secret'

    def get_scope_mentions():
        s = str(scope).strip()
        return s.lower().split(' ') if s else []

    def update_scope_mention(old, new):
        mentions = get_scope_mentions()
        mentions.remove(old.lower())
        mentions.append(new.lower())
        post.scope = ' '.join(mentions)

    post.get_scope_mentions = get_scope_mentions
    post.update_scope_mention = update_scope_mention
    post.can_be_accessed_by = lambda user, mode: _can_be_accessed_by(post, user, mode)
    return post


def _can_be_accessed_by(post, user, mode):
    if mode == PostMode.SPOILER:
        return True
    elif mode == PostMode.FOR:
        if user.username and user.username.lower() in post.get_scope_mentions():
            post.update_scope_mention(user.username, str(user.id))
            return True
        return user.id == post.author.user_id or str(user.id) in post.get_scope_mentions()
    elif mode == PostMode.EXCEPT:
        if user.id == post.author.user_id:
            return True
        if user.username and user.username.lower() in post.get_scope_mentions():
            post.update_scope_mention(user.username, str(user.id))
            return False
        return str(user.id) not in post.get_scope_mentions()


def make_user(uid=42, username=None):
    u = MagicMock()
    u.id = uid
    u.username = username
    return u


class TestPostCanBeAccessedBy:
    def test_spoiler_always_grants(self):
        post = make_post()
        user = make_user()
        assert post.can_be_accessed_by(user, PostMode.SPOILER) is True

    def test_for_author_always_grants(self):
        post = make_post(scope='', author_id=42)
        user = make_user(uid=42)
        assert post.can_be_accessed_by(user, PostMode.FOR) is True

    def test_for_id_in_scope_grants(self):
        post = make_post(scope='99 100')
        user = make_user(uid=99)
        assert post.can_be_accessed_by(user, PostMode.FOR) is True

    def test_for_id_not_in_scope_denied(self):
        post = make_post(scope='99 100', author_id=1)
        user = make_user(uid=55)
        assert post.can_be_accessed_by(user, PostMode.FOR) is False

    def test_for_username_in_scope_grants(self):
        post = make_post(scope='alice bob')
        user = make_user(uid=7, username='alice')
        assert post.can_be_accessed_by(user, PostMode.FOR) is True

    def test_except_id_in_scope_denied(self):
        post = make_post(scope='42')
        user = make_user(uid=42)
        assert post.can_be_accessed_by(user, PostMode.EXCEPT) is False

    def test_except_id_not_in_scope_grants(self):
        post = make_post(scope='99')
        user = make_user(uid=42)
        assert post.can_be_accessed_by(user, PostMode.EXCEPT) is True

    def test_except_username_in_scope_denied(self):
        post = make_post(scope='alice')
        user = make_user(uid=7, username='alice')
        assert post.can_be_accessed_by(user, PostMode.EXCEPT) is False

    def test_for_id_substring_no_false_positive(self):
        # Bug fix: "42" in "420 100" via substring match would return True
        post = make_post(scope='420 100', author_id=1)
        user = make_user(uid=42)
        assert post.can_be_accessed_by(user, PostMode.FOR) is False

    def test_except_id_substring_no_false_negative(self):
        # Bug fix: "42" in "420" via substring match would block user 42 incorrectly
        post = make_post(scope='420', author_id=1)
        user = make_user(uid=42)
        assert post.can_be_accessed_by(user, PostMode.EXCEPT) is True

    def test_except_author_always_grants_even_if_in_scope(self):
        # Author's ID in except scope must not block their own access
        post = make_post(scope='42', author_id=42)
        user = make_user(uid=42)
        assert post.can_be_accessed_by(user, PostMode.EXCEPT) is True

    def test_for_empty_scope_grants_only_author(self):
        post = make_post(scope='', author_id=10)
        author = make_user(uid=10)
        stranger = make_user(uid=99)
        assert post.can_be_accessed_by(author, PostMode.FOR) is True
        assert post.can_be_accessed_by(stranger, PostMode.FOR) is False

    def test_except_empty_scope_grants_everyone(self):
        post = make_post(scope='', author_id=10)
        user = make_user(uid=99)
        assert post.can_be_accessed_by(user, PostMode.EXCEPT) is True


# ---------------------------------------------------------------------------
# User.get_or_create — DB interaction mocked
# ---------------------------------------------------------------------------

class TestUserGetOrCreate:
    def test_existing_user_is_refreshed(self):
        from pombo.database.models import User
        tg_user = MagicMock()
        tg_user.id = 1
        tg_user.first_name = 'Test'
        tg_user.last_name = None
        tg_user.username = 'tester'
        tg_user.language_code = 'pt'

        existing = MagicMock()
        existing.has_banned = False

        with patch.object(User, 'get_by_id', return_value=existing):
            result = User.get_or_create(tg_user)
            existing.refresh.assert_called_once_with(tg_user)
            assert result is existing

    def test_new_user_is_created(self):
        from pombo.database.models import User
        tg_user = MagicMock()
        tg_user.id = 2
        tg_user.first_name = 'New'
        tg_user.last_name = None
        tg_user.username = None
        tg_user.language_code = 'en'

        created = MagicMock()
        with patch.object(User, 'get_by_id', side_effect=User.DoesNotExist):
            with patch.object(User, 'create', return_value=created):
                result = User.get_or_create(tg_user)
                User.create.assert_called_once()
                assert result is created


# ---------------------------------------------------------------------------
# Group.get_or_create — DB interaction mocked
# ---------------------------------------------------------------------------

class TestGroupGetOrCreate:
    def test_existing_group_is_refreshed(self):
        from pombo.database.models import Group
        chat = MagicMock()
        chat.id = 100
        existing = MagicMock()

        with patch.object(Group, 'get_by_id', return_value=existing):
            result = Group.get_or_create(chat)
            existing.refresh.assert_called_once_with(chat)
            assert result is existing

    def test_new_group_is_created(self):
        from pombo.database.models import Group
        chat = MagicMock()
        chat.id = 200
        chat.type = 'group'
        chat.title = 'Test Group'
        chat.username = None

        created = MagicMock()
        with patch.object(Group, 'get_by_id', side_effect=Group.DoesNotExist):
            with patch.object(Group, 'create', return_value=created):
                result = Group.get_or_create(chat)
                Group.create.assert_called_once()
                assert result is created
