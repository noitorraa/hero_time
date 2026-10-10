class Enemy:
    def __init__(self, name):
        self.name = name
        self.stats = {"hp": 100, "damage": 15}
        self.equipment = {"boots": None, "chest": None, "legs": None, "helmet": None}

    def __str__(self):
        return f"{self.name}: {self.stats}"

    def is_alive(self):
        return self.stats["hp"] > 0

    def take_damage(self, amount):
        self.stats["hp"] = max(self.stats["hp"] - amount, 0)

    def attack(self, target):
        target.take_damage(self.stats["damage"])
