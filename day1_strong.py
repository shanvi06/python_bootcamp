num=int(input("enter the number"))
temp=num
sum=0
while(temp>0):
    i=1
    fact=1
    rem=temp%10
    while(i<=rem):
        fact=fact*i
        i+=1
    sum+=fact
    temp=temp//10    
if sum==num:
    print("strong")
else:
    print("not strong")    