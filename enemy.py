import random


class Enemy:
    def __init__(self, name, loot_table=None):
        self.name = name
        self.stats = {"hp": 100, "damage": 8, "xp_reward": 125}
        self.equipment = {"boots": None, "chest": None, "legs": None, "helmet": None}
        self.loot_table = loot_table or []

    def __str__(self):
        return f"{self.name}: {self.stats}"

    def is_alive(self):
        return self.stats["hp"] > 0

    def take_damage(self, amount):
        self.stats["hp"] = max(self.stats["hp"] - amount, 0)

    def attack(self, target):
        target.take_damage(self.stats["damage"])

    def roll_loot(self):
        dropped = []
        for entry in self.loot_table:
            if random.randint(1, 100) <= entry["chance"]:
                dropped.append(entry["item"])
        return dropped
