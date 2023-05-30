import datetime


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
