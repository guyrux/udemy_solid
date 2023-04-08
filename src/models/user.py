class User:
    def __init__(self, username, email) -> None:
        self._username = username
        self._email = email

    @staticmethod
    def work():
        raise NotImplementedError


class Manager(User):
    def __init__(self, username, email) -> None:
        super().__init__(username, email)

    @staticmethod
    def work():
        return 'Paying bills...'


class Member(User):
    def __init__(self, username, email) -> None:
        super().__init__(username, email)

    def list_member(self):
        return [self._username, self._email]

    @staticmethod
    def work():
        return 'Coding...'
