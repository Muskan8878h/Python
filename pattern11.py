n=int(input())
i=1
a=n
while i<=n:
    j=1
    k=chr(ord('A')+a-1)
    while j<=i:
        print(chr(ord(k)+j-1),end=" ")
        j+=1
    print()
    a-=1
    i+=1

#E
#D E
#C D E
#B C D E
#A B C D E