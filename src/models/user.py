class User:
    def __init__(self, username, email) -> None:
        self._username = username
        self._email = email


class Manager(User):
    def __init__(self, username, email) -> None:
        super().__init__(username, email)


class Member(User):
    def __init__(self, username, email) -> None:
        super().__init__(username, email)

    def list_member(self):
        return [self._username, self._email]
