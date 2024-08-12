for i in range(1,1000):
     n = len(str(i))
     n1 = i
     sum = 0
     while n1 > 0:
        digit = n1 % 10
        sum += digit ** n
        n1 //= 10

     if i == sum:
        print(i)