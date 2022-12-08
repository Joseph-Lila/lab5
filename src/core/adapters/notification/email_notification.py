import smtplib

from src.core.adapters.notification.abstract_notification import AbstractNotification, DEFAULT_HOST, DEFAULT_PORT


class EmailNotification(AbstractNotification):
    def __init__(self, smtp_host=DEFAULT_HOST, port=DEFAULT_PORT):
        self.server = smtplib.SMTP(smtp_host, port=port)
        self.server.noop()

    def send(self, destination, message):
        msg = f"Subject: transport service notification\n{message}"
        self.server.sendmail(
            from_addr="transports@example.com",
            to_addrs=[destination],
            msg=msg
        )
