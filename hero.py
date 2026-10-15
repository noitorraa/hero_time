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
        self.inventory = []
        self.equipment = {"boots": None, "chest": None, "legs": None, "helmet": None}

    @property
    def gold(self):
        return sum(i["amount"] for i in self.inventory if i["type"] == "gold")

    def add_item(self, item):
        self.inventory.append(item)
        if item["type"] == "gold":
            print(f"Получено золото: {item['amount']}")
        else:
            print(f"Получен предмет: {item.get('name', item['type'])}")

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

    def gain_xp(self, amount_xp):
        lvl_before_take_xp = int(self.stats["level"])
        self.stats["xp"] += amount_xp
        while self.stats["xp"] >= self.stats["max_xp"]:
            self.stats["xp"] = self.stats["xp"] - self.stats["max_xp"]
            self.level_up()
        print(
            f"Получено опыта: {amount_xp}. Уровень {lvl_before_take_xp}→{self.stats['level']}"
        )

    def attack(self, target):
        target.take_damage(self.stats["damage"])

    def is_alive(self):
        return self.stats["hp"] > 0

    def fight(self, enemy):
        print(f"Вы напали на {enemy.name}")
        while self.is_alive():
            input("Нажмите Enter чтобы атаковать противника")
            self.attack(enemy)
            print(f"{self.name} наносит {enemy.name} {self.stats['damage']} урона")
            if enemy.is_alive():
                enemy.attack(self)
                print(f"{enemy.name} наносит {self.name} {enemy.stats['damage']} урона")
            else:
                break
        if self.is_alive():
            print("Вы одерживаете победу!")
            self.gain_xp(enemy.stats["xp_reward"])
            for item in enemy.roll_loot():
                self.add_item(item)
            return True
        return False

    def explore(self):
        while True:
            enemy = self.spawn_enemy()
            won = self.fight(enemy)
            if won:
                if (
                    input("Продолжить путь? [y] Отправиться в лагерь [n]").lower()
                    == "n"
                ):
                    print("Вы возвращаетесь в лагерь")
                    break
            else:
                print("Вы погибли!")
                break

    def spawn_enemy(self):
        return Enemy(
            "Гоблин",
            loot_table=[
                {"item": {"type": "gold", "amount": 10}, "chance": 100},  # всегда
                {"item": {"type": "gold", "amount": 25}, "chance": 30},  # бонус
            ],
        )


if __name__ == "__main__":
    hero = Hero(input("Имя вашего героя? "))
    hero.explore()
