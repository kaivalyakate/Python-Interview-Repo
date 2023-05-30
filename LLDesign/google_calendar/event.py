import datetime
from typing import List
from LLDesign.google_calendar.user import User
from LLDesign.google_calendar.common import EventColor


class Event:

    def __init__(
            self,
            id: str,
            start: datetime.datetime,
            end: datetime.datetime,
            owner: User,
            location: str,
            invitees: List[User],
            title: str,
            description: str,
            color: EventColor,
            all_day: bool,
            recurrence
    ):
        self.id = id
        self.start = start
        self.end = end
        self.owner = owner
        self.location = location
        self.invitees = invitees
        self.title = title
        self.all_day = all_day
        self.description = description
        self.color = color

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


class EventRequest:

    def __init__(self, event: Event, user: User):
        self.event = event
        self.user = user
