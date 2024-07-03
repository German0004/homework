# ІНКАПСУЛЯЦІЯ

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Only number !!!")
        self.__balance = value


a = BankAccount("Franko", 10000)

# print(a.balance)
print(a.get_balance()) # Ми не можемо звертатися до змінної  print(a.balance), але можемо використовувати get_balance()
                        # для класу і для змінної balance

# a.set_balance("qqqq") # Буде виведено ValueError: Only number !!!
print(a.get_balance())