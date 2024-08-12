class bankaccount:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
    def withdraw (self,amount):
        if amount>0 and self.balance>=amount:
            self.balance-=amount
    def get_balance(self):
        return self.balance
account=bankaccount(1000)
account.deposit(500)
account.withdraw(200)
print(f"account balance:{account.get_balance()}")
