class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издает звук.")

    def eat(self):
        print(f"{self.name} ест.")
class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} поет чирик-чирик!")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} рычит!")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} шипит!")
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, {animal.age} лет")

    def show_staff(self):
        for staff_member in self.staff:
            print(staff_member.name)
class Staff:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Staff):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian(Staff):
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")
# Создаем животных
parrot = Bird("Попугай", 2)
lion = Mammal("Лев", 5)
snake = Reptile("Удав", 4)

# Создаем сотрудников
keeper = ZooKeeper("Анна")
vet = Veterinarian("Доктор Иванов")

# Создаем зоопарк
my_zoo = Zoo()
my_zoo.add_animal(parrot)
my_zoo.add_animal(lion)
my_zoo.add_animal(snake)

my_zoo.add_staff(keeper)
my_zoo.add_staff(vet)

# Проверяем животных
animal_sound(my_zoo.animals)

# Проверяем работу сотрудников
keeper.feed_animal(lion)
vet.heal_animal(snake)

# Показываем всех животных и сотрудников
my_zoo.show_animals()
my_zoo.show_staff()
