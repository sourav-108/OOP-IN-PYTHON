class AppSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.theme = "light"
        return cls._instance


settings_a = AppSettings()
settings_b = AppSettings()

settings_a.theme = "dark"
print(settings_b.theme)  # dark
print(settings_a is settings_b)  # True