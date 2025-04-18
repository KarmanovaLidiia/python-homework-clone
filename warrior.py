class Warrior:
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1

    def hit(self):
        print(f"{self.name} бьет кого-то")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f"Имя воина: {self.name}")
        print(f"Цвет волос: {self.hair_color}")
        print(f"Сила: {self.power}")
        print(f"Выносливость: {self.endurance}")

# создаём воина
petya = Warrior("Петя", 50, 40, "рыжий")
petya.info()
petya.eat()
petya.hit()
petya.sleep()
petya.info()
