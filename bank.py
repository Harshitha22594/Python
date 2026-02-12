# Q1. Banking System (Finance Domain)
# Design a BankAccount class.
# Methods to think about:
# • withdraw money (object method)
# • deposit money (object method)
# • display account details (object method)
# • update minimum balance (class method

class bank:
    bname = "SBI"
    loc = "Hyderabad"
    balance = 100000
    def __init__ (self, name, bid, age, acno, balance):
        self.name = name
        self.bid = bid 
        self.age = age
        self.acno = acno
        self.balance = balance

    def withdraw(self, amount):
        if amount > 0:
            if amount < self.balance:
                self.balance = self.balance - amount
                print("success")
            else:
                print("insufficient balance")
        else:
            print("no balance")
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount 
            print("success")
        else:
            print("invalid amount")
    def display(self):
        print("bname:", self.bname, "loc:", self.loc, "balance:", self.balance)
    @classmethod
    def min_balance(cls):
        if cls.balance < 5000:
            print("balance is less than minimum balance")
        else:
            print("balance is sufficient")
        
b1 = bank("Harshitha", 1, 21, 1234567890, 10000)

b1.display()
b1.withdraw(6000) 
b1.min_balance()
b1.deposit(2000)
b1.display()

