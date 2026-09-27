class LoginAccount:
    def __init__(self, password):
        self.__password = password
        self.__failed_attempts = 0
        self.__locked = False

    def login(self, entered_password):
        if self.__locked:
            return "Account locked"

        if entered_password == self.__password:
            self.__failed_attempts = 0
            return "Login successful"

        self.__failed_attempts += 1

        if self.__failed_attempts >= 3:
            self.__locked = True
            return "Account locked"

        return "Incorrect password"


account = LoginAccount("blueBike7")
print(account.login("wrong"))
print(account.login("wrong"))
print(account.login("wrong"))  # Account locked