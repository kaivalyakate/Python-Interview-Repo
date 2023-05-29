import datetime
from typing import List


class User:

    def __init__(
            self,
            user_id: str,
            email: str,
            birthday: datetime.date
    ):
        self.user_id = user_id
        self.email = email
        self.birthday = birthday
        self.event_requests = []

    def accept_event(self):
        pass


class Event:

    def __init__(
            self,
            start: datetime.datetime,
            end: datetime.datetime,
            owner: User,
            location: str,
            invitees: List[User],
            title: str
    ):
        self.start = start
        self.end = end
        self.owner = owner
        self.location = location
        self.invitees = invitees
        self.title = title

    @classmethod
    def Meeting(cls, start: datetime.datetime, end: datetime.datetime):
        pass

    @classmethod
    def Holiday(cls):
        pass

    @classmethod
    def Birthday(cls):
        pass

    @classmethod
    def Reminder(cls):
        pass

    @property
    def date(self):
        return None


class Calendar:

    def __init__(self, user: User):
        self.user = user
        self.events = []

    def get_events(self):
        return self.events

    def add_event(self, event: Event):
        # Validate Event Parameters
        self.events.append(event)


class CalendarManager:

    @classmethod
    def get_calendar(cls, user: User):
        return Calendar(user=user)
