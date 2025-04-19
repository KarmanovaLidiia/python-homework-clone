class Car:
    def __init__(self, make, model):
        self.public_make = make                # открытый
        self._protected_model = model          # защищённый
        self.__private_year = 2022             # приватный
    def public_method(self):
        return f"Открытый метод. Машина: {self.public_make} {self._protected_model}"

    def _protected_method(self):
        return "Защищённый метод"

    def __private_method(self):
        return "Приватный метод"
class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def get_details(self):
        return f"{self.public_make} {self._protected_model}, батарея: {self.battery_size} kWh"
tesla = ElectricCar("Tesla", "Model S", 100)

# ✅ Публичное — можно спокойно использовать:
print(tesla.public_make)
print(tesla.public_method())
print(tesla.get_details())

# ⚠️ Защищённое — можно, но не очень красиво:
print(tesla._protected_model)
print(tesla._protected_method())

# ❌ Приватное — напрямую будет ошибка:
# print(tesla.__private_year)  # Ошибка

# 🧪 Но можно получить его вот так (не рекомендуется):
print(tesla._Car__private_year)
