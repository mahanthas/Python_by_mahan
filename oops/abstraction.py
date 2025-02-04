from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def deposit():
        pass

    @abstractmethod
    def withdraw():
        pass


class BankAcount(Bank):
    __balance = 100000
    def __init__(self,account_number):
        self.account_number = account_number


    def deposit(self,dep_amt):
        self.dep_amt = dep_amt
        self.__balance = self.__balance + self.dep_amt

    def withdraw(self,with_amt):
        self.with_amt = with_amt
        if (with_amt < self.__balance):
            self.__balance = self.__balance - self.with_amt
        else:
            print("Low Balance")

    def show_balance(self):
        print(f"Your Acoount Balance is : {self.__balance}")

b1 = BankAcount(12345)
b1.show_balance()
b1.deposit(10000)
b1.show_balance()
b1.withdraw(30000)
b1.show_balance()
b1.withdraw(1000000)
