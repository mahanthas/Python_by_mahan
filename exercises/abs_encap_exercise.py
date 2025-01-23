"""
    Questions:
            1. Create Account class with 2 attributes - balance & account no.
                and Create methods for debit, credit & printing the balance.
"""

class Account:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self,debit):
        self.debit = debit
        print("Your account ",self.acc_no,"has been debited with",self.debit)
        self.balance = self.balance - self.debit
        print("your account balance after debit is ",self.print_balance())
    def credit(self,credit):
        self.credit = credit
        print("Your account ",self.acc_no,"has been credited with",self.credit)
        self.balance = self.balance + self.credit
        print("your account balance after credit is ",self.print_balance())
    def print_balance(self):
        return self.balance

acc1 = Account(250000,12345)
print(acc1.balance,acc1.acc_no)

acc1.credit(20000)
acc1.debit(10000)