from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message, recipient):
        pass


class EmailNotification(Notification):
    def send(self, message, recipient):
        return f"Email to {recipient}: {message}"


class SMSNotification(Notification):
    def send(self, message, recipient):
        return f"SMS to {recipient}: {message}"


def send_alert(channel, message, recipient):
    print(channel.send(message, recipient))


send_alert(EmailNotification(), "Order shipped", "customer@example.com")
send_alert(SMSNotification(), "Order shipped", "+8801234567890")