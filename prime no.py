n=int(input())
i=1
count=0
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print("prime ")
else:
    print("composit")





n = int(input())
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("prime")
else:
    print("composite")