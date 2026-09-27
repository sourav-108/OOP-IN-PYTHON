class User:
    def __init__(self, password):
        self.__password = password

    def check_password(self, attempt):
        return attempt == self.__password


user = User("abc123")
print(user.check_password("abc123"))  # True