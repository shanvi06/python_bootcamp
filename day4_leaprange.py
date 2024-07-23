a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    if (i%400==0) or (i%4==0 and i%100!=0):
        print(i,end=" ")