class EmailNotification:
    def send(self, message):
        return f"Email sent: {message}"


class SMSNotification:
    def send(self, message):
        return f"SMS sent: {message}"


def notify(channel, message):
    print(channel.send(message))


notify(EmailNotification(), "Your order has shipped")
notify(SMSNotification(), "Your order has shipped")