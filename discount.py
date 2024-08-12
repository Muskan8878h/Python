a=int(input("amount"))
if a<100:
    print("no discount applied")
    print("final amount",a)
elif 100<a<200:
    print("discount applied=10%")
    print("final amount",a-(a*10/100))
elif 200<a<300:
    print("discount applied=15%")
    print("final amount",a-(a*15/100))
else:
    print("discount applied=20%")
    print("final amount",a-(a*20/100))

