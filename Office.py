class Office:
    def __init__(self):
        self.public_file = "Инструкция на стене"
        self._protected_file = "Папка в шкафу с табличкой"
        self.__private_file = "Запертый сейф"

    def get_private_file(self):
        return self.__private_file

    def set_private_file(self, value):
        self.__private_file = value
of = Office()
print(of.public_file)         # Всё видно!
print(of._protected_file)     # Тоже видно, но с предупреждением
# print(of.__private_file)    # ❌ Ошибка!

# Получаем доступ к секрету по запросу
print(of.get_private_file())

# Меняем секрет, как через администратора
of.set_private_file("Новая тайна")
print(of.get_private_file())
