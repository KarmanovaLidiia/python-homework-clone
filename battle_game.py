import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(10, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        player_name = input("Введите имя героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print(f"\nБитва начинается между {self.player.name} и {self.computer.name}!\n")
        round_num = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n--- Раунд {round_num} ---")
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"\n{self.computer.name} побеждён!")
                break

            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"\n{self.player.name} побеждён!")
                break

            print(f"Здоровье {self.player.name}: {self.player.health}")
            print(f"Здоровье {self.computer.name}: {self.computer.health}")
            round_num += 1

        print("\nИгра окончена.")
        winner = self.player.name if self.player.is_alive() else self.computer.name
        print(f"Победитель: {winner}!")

if __name__ == "__main__":
    game = Game()
    game.start()
