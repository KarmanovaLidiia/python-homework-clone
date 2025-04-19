class Account:
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счёт. Сумма на счёте — {self.balance} руб.")
        else:
            print("Сумма пополнения должна быть больше 0.")

    def withdraw(self, money):
        if money > self.balance:
            print("Недостаточно средств на счёте.")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} руб. Остаток на счёте: {self.balance} руб.")

    def all_balance(self):
        print(f"Текущий баланс — {self.balance} руб.")


# --- Вот здесь начинается тестирование ---
man = Account(id="12323132", balance=755)

man.all_balance()
man.deposit(355)
man.withdraw(188)
man.withdraw(777)
man.all_balance()
