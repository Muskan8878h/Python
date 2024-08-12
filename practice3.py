temp=int(input("Enter Temperature :"))
unit=input("Enter Unit : ")
if unit=='c':
    print("Temperature in Celsius is :",9/5*temp+32)
else:
    print("Temperature in Fahrenheit is :",(temp-32)*5/9)