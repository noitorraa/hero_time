from enemy import Enemy


class Hero:
    def __init__(self, name):
        self.name = name
        self.stats = {
            "hp": 100,
            "damage": 10,
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
        print(f"Получен урон {amount} очков")

    def heal(self, amount):
        self.stats["hp"] = min(self.stats["hp"] + amount, self.stats["max_hp"])
        print(f"Получено лечение на {amount} очков")

    def level_up(self):
        self.stats["level"] += 1
        self.stats["max_xp"] = int(self.stats["max_xp"] * 1.5)
        self.stats["max_hp"] = int(self.stats["max_hp"] * 1.2)
        self.stats["damage"] = int(self.stats["damage"] * 1.1)
        self.stats["max_mana"] = int(self.stats["max_mana"] * 1.2)
        print(f"Вы повысили уровень! ваши актуальные характеристики: {self}")

    def gain_xp(self, amount_xp):
        print(f"Получено опыта: {amount_xp}")
        self.stats["xp"] += amount_xp
        while self.stats["xp"] >= self.stats["max_xp"]:
            self.stats["xp"] = self.stats["xp"] - self.stats["max_xp"]
            self.level_up()

    def attack(self, target):
        target.take_damage(self.stats["damage"])

    def is_alive(self):
        return self.stats["hp"] > 0

    def fight(self, hero, enemy):
        print(f"Вы атаковали {enemy.name}")
        while self.is_alive() and enemy.is_alive():
            if input():
                self.attack(enemy)
            print(f"{self.name} наносит {enemy.name} {self.stats['damage']} урона")
            enemy.attack(hero)
            print(f"{enemy.name} наносит {hero.name} {enemy.stats['damage']} урона")
        return "Вы одерживаете победу!" if self.is_alive() else "Вы погибли!"


if __name__ == "__main__":
    hero = Hero(input("Имя вашего героя? "))
    enemy = Enemy("Гоблин")
    print(hero.fight(hero, enemy))
