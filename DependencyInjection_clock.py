from datetime import datetime


class SystemClock:
    def now(self):
        return datetime.now()


class ReminderService:
    def __init__(self, clock):
        self.clock = clock

    def message(self):
        current_time = self.clock.now()
        return f"Reminder checked at {current_time:%H:%M}"


reminders = ReminderService(SystemClock())
print(reminders.message())