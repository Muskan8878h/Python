import random
mini=int(input("mini no.is"))
maxi=int(input("maxi no.is"))
secret=random.randint(1,100)
while True:
        guess=int(input("guess"))
        if guess<secret:
            print("to low try again")
        elif guess>secret:
            print("to high try again")
        else:
            print("congratulation ,do you want to try again")

