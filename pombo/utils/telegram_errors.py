"""Classify Telegram broadcast failures without disabling valid recipients."""


def is_permanent_recipient_error(error_code, message):
    """Only unavailable recipients should be removed from future broadcasts."""
    text = (message or '').lower()
    if error_code == 403:
        return any(reason in text for reason in (
            'bot was blocked by the user',
            'bot was kicked from the',
            'user is deactivated',
            'forbidden: bot is not a member',
        ))
    if error_code == 400:
        return 'chat not found' in text or 'user not found' in text
    return False
