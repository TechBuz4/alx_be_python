#Understand the fundamentals of OOP in Python by implementing a BankAccount class
# that encapsulates banking operations. Use command line arguments to interact 
# with instances of this class.

class BankAccount():
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        return self.account_balance
    def withdraw(self, amount):
        if amount > self.account:
            return False
        else:
            self.account_balance -= amount
            return True
    def display_balance(self):
        print(f"Your current balance is {self.account_balance:.2f}")
