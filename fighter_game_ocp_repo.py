# Шаг 1: Абстрактный класс оружия
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "удар мечом"

class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"


# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return f"{self.name} наносит {self.weapon.attack()}"
        else:
            return f"{self.name} не выбрал оружие"


# Класс Monster
class Monster:
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def take_damage(self):
        self.hp = 0
        return f"Монстр {self.name} побежден!"


# Шаг 4: Демонстрация боя
if __name__ == "__main__":
    hero = Fighter("Боец")
    monster1 = Monster("Гоблин")

    # Боец выбирает меч
    hero.change_weapon(Sword())
    print("Боец выбирает меч.")
    print(hero.attack())
    print(monster1.take_damage())

    print("\n")

    # Боец выбирает лук
    monster2 = Monster("Орк")
    hero.change_weapon(Bow())
    print("Боец выбирает лук.")
    print(hero.attack())
    print(monster2.take_damage())
