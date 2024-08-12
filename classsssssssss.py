class car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def get_age(self):
        current_year=2023
        age=current_year - self.year
        return age
    def display_info(self):
        return f"{self.year}{self.make}{self.model}"
car1=car("toyota" ,"camry" ,2020)
print(car1.display_info())
print(f"car age: {car1.get_age()}years")


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("John",36)
print(p1.name)
print(p1.age)


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





