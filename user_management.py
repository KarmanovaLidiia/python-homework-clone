# user_management.py

# 1. Базовый класс User с инкапсуляцией
class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'  # стандартный доступ для обычного сотрудника

    # Геттеры (чтобы получить данные)
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Сеттер для изменения имени (пример работы с инкапсуляцией)
    def set_name(self, new_name):
        self.__name = new_name


# 2. Класс Admin наследуется от User и добавляет методы управления пользователями
class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__admin_access_level = 'admin'
        self.__users = []  # Список для хранения пользователей

    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                self.__users.remove(user)
                print(f"Пользователь с ID {user_id} удалён.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    def list_users(self):
        print("\nТекущий список пользователей:")
        for user in self.__users:
            print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Доступ: {user.get_access_level()}")


# 3. Демонстрация работы
if __name__ == "__main__":
    admin = Admin(0, "Админ")
    user1 = User(1, "Алексей")
    user2 = User(2, "Мария")

    admin.add_user(user1)
    admin.add_user(user2)

    admin.list_users()

    admin.remove_user(1)
    admin.list_users()
