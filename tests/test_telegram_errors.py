import unittest

from pombo.utils.telegram_errors import is_permanent_recipient_error


class BroadcastErrorTests(unittest.TestCase):
    def test_user_blocked(self):
        self.assertTrue(is_permanent_recipient_error(403, 'Forbidden: bot was blocked by the user'))

    def test_group_removed(self):
        self.assertTrue(is_permanent_recipient_error(403, 'Forbidden: bot was kicked from the supergroup'))

    def test_missing_chat(self):
        self.assertTrue(is_permanent_recipient_error(400, 'Bad Request: chat not found'))

    def test_rate_limit_does_not_disable(self):
        self.assertFalse(is_permanent_recipient_error(429, 'Too Many Requests: retry after 5'))

    def test_temporary_error_does_not_disable(self):
        self.assertFalse(is_permanent_recipient_error(500, 'Internal Server Error'))

    def test_other_bad_request_does_not_disable(self):
        self.assertFalse(is_permanent_recipient_error(400, 'Bad Request: message is too long'))

    def test_ambiguous_forbidden_does_not_disable(self):
        self.assertFalse(is_permanent_recipient_error(403, 'Forbidden: unknown reason'))


if __name__ == '__main__':
    unittest.main()
