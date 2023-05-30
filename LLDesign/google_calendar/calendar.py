from typing import List
from LLDesign.google_calendar.user import User
from LLDesign.google_calendar.event import Event


class Calendar:

    def __init__(self, user: User):
        self.user = user
        self.events: List[Event] = []
        self.event_requests: List = []

    def get_events(self):
        return self.events

    def accept_event(self, event: Event):
        # Accept an event request and add the event to the current user's calendar
        self.events.append(event)

    def reject_event(self):
        # Reject an event request. Remove the request from the user's calendar
        pass

    def update_event(self):
        pass

    def add_event(self):
        # Add an event to the User's calendar
        pass

    def delete_event(self):
        # Delete an event from the user's calendar
        pass

    def invite(self, users: List[User], event: Event):
        # Invite Users to an event. Send event requests
        pass


class CalendarManager:

    @classmethod
    def get_calendar(cls, user: User):
        # read calendar from db
        return Calendar(user=user)

