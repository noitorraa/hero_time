class Hero:
    def __init__(self, name):
        self.name = name
        self.stats = {
            "hp": 100,
            "max_hp": 100,
            "mana": 50,
            "max_mana": 50,
            "xp": 0,
            "max_xp": 10,
            "level": 1,
        }
        self.equipment = {"boots": None, "chest": None, "legs": None, "helmet": None}

    def __str__(self):
        return f"{self.name}: {self.stats}"

    def take_damage(self, amount):
        self.stats["hp"] = max(self.stats["hp"] - amount, 0)

    def heal(self, amount):
        self.stats["hp"] = min(self.stats["hp"] + amount, self.stats["max_hp"])


hero = Hero(input("Имя вашего героя? "))
print(hero)
hero.take_damage(50)
print(f"Получен урон 50! Твои характеристики: {hero}")
hero.heal(50)
print(f"Получено лечение 50! Твои характеристики: {hero}")
