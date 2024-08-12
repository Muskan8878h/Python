import random
print("check balance")
print("deposit funds")
print("withdraw funds")
print("exit")
balance=random.randint(1000,10000)
while True:
    print("enter choice between 1 to 4")
    choice=int(input())
    if choice==1:
        print("current account balance:",balance)
    elif choice==2:
        print("enter ammount to deposite:")
        print("balance",balance)
        deposit=int(input())
        a_balance=balance+deposit
        print("current balance ",a_balance)
    elif choice==3:
        print("enter withdraw ammount")
        print("balance",balance)
        withdraw=int(input())
        u_balance=balance-withdraw
        print("current balance",u_balance)
    else:
        print("exit")




