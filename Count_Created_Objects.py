class Player:
    count = 0

    def __init__(self, name):
        self.name = name
        Player.count += 1


Player("Angan")
Player("Durjoy")
print(Player.count)  # 2