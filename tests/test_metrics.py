import pytest
from unittest.mock import MagicMock, patch
from datetime import datetime, timedelta, timezone


def make_qs(count=0, rows=None):
    qs = MagicMock()
    qs.where.return_value = qs
    qs.order_by.return_value = qs
    qs.limit.return_value = qs
    qs.count.return_value = count
    qs.__iter__ = lambda self: iter(rows or [])
    return qs


def make_row(first_dt, last_dt):
    row = MagicMock()
    row.first_interaction_time = first_dt
    row.last_interaction_time = last_dt
    return row


# ---------------------------------------------------------------------------
# User.count_active_since
# ---------------------------------------------------------------------------

class TestCountActiveSince:
    def test_returns_count_from_db(self):
        from pombo.database.models import User
        qs = make_qs(count=42)
        with patch.object(User, 'select', return_value=qs):
            assert User.count_active_since(1) == 42

    def test_zero_active(self):
        from pombo.database.models import User
        qs = make_qs(count=0)
        with patch.object(User, 'select', return_value=qs):
            assert User.count_active_since(7) == 0

    def test_where_called_with_cutoff(self):
        from pombo.database.models import User
        qs = make_qs(count=5)
        with patch.object(User, 'select', return_value=qs):
            User.count_active_since(30)
            qs.where.assert_called_once()


# ---------------------------------------------------------------------------
# User.count_with_dialog
# ---------------------------------------------------------------------------

class TestCountWithDialog:
    def test_returns_dialog_count(self):
        from pombo.database.models import User
        qs = make_qs(count=15)
        with patch.object(User, 'select', return_value=qs):
            assert User.count_with_dialog() == 15

    def test_zero_with_dialog(self):
        from pombo.database.models import User
        qs = make_qs(count=0)
        with patch.object(User, 'select', return_value=qs):
            assert User.count_with_dialog() == 0

    def test_where_called(self):
        from pombo.database.models import User
        qs = make_qs(count=0)
        with patch.object(User, 'select', return_value=qs):
            User.count_with_dialog()
            qs.where.assert_called_once()


# ---------------------------------------------------------------------------
# User.retention_rate
# ---------------------------------------------------------------------------

class TestRetentionRate:
    def _now(self):
        return datetime.now(timezone.utc)

    def test_empty_cohort_returns_zero_zero(self):
        from pombo.database.models import User
        qs = make_qs(rows=[])
        with patch.object(User, 'select', return_value=qs):
            retained, total = User.retention_rate(7)
            assert retained == 0
            assert total == 0

    def test_user_who_returned_counts_as_retained(self):
        from pombo.database.models import User
        now = self._now()
        row = make_row(now - timedelta(days=10), now - timedelta(days=2))
        qs = make_qs(rows=[row])
        with patch.object(User, 'select', return_value=qs):
            retained, total = User.retention_rate(7)
            assert total == 1
            assert retained == 1

    def test_user_who_never_returned_not_retained(self):
        from pombo.database.models import User
        now = self._now()
        row = make_row(now - timedelta(days=10), now - timedelta(days=10) + timedelta(hours=1))
        qs = make_qs(rows=[row])
        with patch.object(User, 'select', return_value=qs):
            retained, total = User.retention_rate(7)
            assert total == 1
            assert retained == 0

    def test_exactly_at_threshold_retained(self):
        from pombo.database.models import User
        now = self._now()
        row = make_row(now - timedelta(days=10), now - timedelta(days=10) + timedelta(days=7))
        qs = make_qs(rows=[row])
        with patch.object(User, 'select', return_value=qs):
            retained, total = User.retention_rate(7)
            assert retained == 1

    def test_mixed_cohort_partial_retention(self):
        from pombo.database.models import User
        now = self._now()
        came_back = make_row(now - timedelta(days=10), now - timedelta(days=2))
        did_not = make_row(now - timedelta(days=10), now - timedelta(days=10) + timedelta(hours=2))
        qs = make_qs(rows=[came_back, did_not])
        with patch.object(User, 'select', return_value=qs):
            retained, total = User.retention_rate(7)
            assert total == 2
            assert retained == 1

    def test_unix_timestamp_integers(self):
        """retention_rate handles raw Unix int timestamps (SQLite tuples mode)."""
        from pombo.database.models import User
        now_ts = datetime.now(timezone.utc).timestamp()
        row = MagicMock()
        row.first_interaction_time = now_ts - 10 * 86400
        row.last_interaction_time = now_ts - 2 * 86400  # 8-day gap >= 7
        qs = make_qs(rows=[row])
        with patch.object(User, 'select', return_value=qs):
            retained, total = User.retention_rate(7)
            assert total == 1
            assert retained == 1

    def test_unix_timestamp_not_retained(self):
        from pombo.database.models import User
        now_ts = datetime.now(timezone.utc).timestamp()
        row = MagicMock()
        row.first_interaction_time = now_ts - 10 * 86400
        row.last_interaction_time = now_ts - 10 * 86400 + 3600  # 1 hour gap < 7 days
        qs = make_qs(rows=[row])
        with patch.object(User, 'select', return_value=qs):
            retained, total = User.retention_rate(7)
            assert retained == 0

    def test_none_timestamps_skipped(self):
        from pombo.database.models import User
        row = make_row(None, None)
        qs = make_qs(rows=[row])
        with patch.object(User, 'select', return_value=qs):
            retained, total = User.retention_rate(7)
            assert total == 1
            assert retained == 0  # skipped, not retained

    def test_d1_d7_d30_thresholds(self):
        from pombo.database.models import User
        now = self._now()
        for days in (1, 7, 30):
            row = make_row(
                now - timedelta(days=days + 5),
                now - timedelta(days=days + 5) + timedelta(days=days),
            )
            qs = make_qs(rows=[row])
            with patch.object(User, 'select', return_value=qs):
                retained, total = User.retention_rate(days)
                assert retained == 1, f'D{days} failed'


# ---------------------------------------------------------------------------
# User.top_users
# ---------------------------------------------------------------------------

class TestTopUsers:
    def test_default_limit_five(self):
        from pombo.database.models import User
        qs = make_qs(rows=[])
        with patch.object(User, 'select', return_value=qs):
            User.top_users()
            qs.limit.assert_called_once_with(5)

    def test_custom_limit(self):
        from pombo.database.models import User
        qs = make_qs(rows=[])
        with patch.object(User, 'select', return_value=qs):
            User.top_users(10)
            qs.limit.assert_called_once_with(10)

    def test_order_by_called(self):
        from pombo.database.models import User
        qs = make_qs(rows=[])
        with patch.object(User, 'select', return_value=qs):
            User.top_users(3)
            qs.order_by.assert_called_once()

    def test_returns_iterable_of_users(self):
        from pombo.database.models import User
        u1, u2 = MagicMock(), MagicMock()
        u1.inline_queries_count = 100
        u2.inline_queries_count = 50
        qs = make_qs(rows=[u1, u2])
        with patch.object(User, 'select', return_value=qs):
            result = list(User.top_users(2))
            assert len(result) == 2
