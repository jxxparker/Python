class BankAccount():
    def __init__(self, int_rate=0, acc_balance=0):
        self.int_rate = int_rate
        self.acc_balance = acc_balance
    
    def deposit(self, amount):
        self.acc_balance += amount
        return self
    
    def withdraw(self,amount):
        if self.acc_balance >= amount:
            self.acc_balance -= amount
        else:
            self.acc_balance -= 5
            print("Insufficient Funds. $5 charged")
        return self
    
    def display_account(self):
        print("Balance : ${}".format(self.acc_balance))
        return self
    
    def yield_interest(self):
        if self.acc_balance > 0:
            self.acc_balance = self.acc_balance + self.acc_balance * self.int_rate
        return self
    
ba1 = BankAccount(.01,1)
ba2 = BankAccount(.10, 500)

ba1.deposit(100).deposit(50).deposit(50).withdraw(100).yield_interest().display_account()
ba2.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account()