num=int(input())
count=len(str(num))
sum,digit=0,0
temp=num
while(temp>0):
    digit=temp%10
    sum+=digit**count
    temp=temp//10
if sum==num:
    print("armstrong  number")
else:
    print("not an armstrong number")        
    