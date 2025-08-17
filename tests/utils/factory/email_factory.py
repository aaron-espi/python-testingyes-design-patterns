import time


class EmailFactory:
    DOMAIN = "@example.com"
    ALREADY_USED_EMAIL_PREFIX = "john.doe"
    UNIQUE_EMAIL_PREFIX = "user"

    @staticmethod
    def already_used_email():
        return EmailFactory.ALREADY_USED_EMAIL_PREFIX + EmailFactory.DOMAIN

    @staticmethod
    def generate_unique_email():
        timestamp = str(int(time.time() * 1000))
        return EmailFactory.UNIQUE_EMAIL_PREFIX + timestamp + EmailFactory.DOMAIN
