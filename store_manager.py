class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


# Пример создания магазинов
store1 = Store("Фрукты и Ягоды", "ул. Яблочная, 12")
store2 = Store("Зелёный Маркет", "ул. Огуречная, 3")
store3 = Store("Всё для дома", "ул. Полезная, 8")

# Добавление товаров
store1.add_item("apple", 0.5)
store1.add_item("banana", 0.8)

store2.add_item("cucumber", 0.3)
store2.add_item("tomato", 0.6)

store3.add_item("broom", 2.5)

# Тестирование методов
print("\n🍎 Цена банана:", store1.get_price("banana"))
store1.update_price("banana", 0.75)
print("🔁 Обновлённая цена банана:", store1.get_price("banana"))
store1.remove_item("apple")
print("❌ Цена яблока после удаления:", store1.get_price("apple"))
