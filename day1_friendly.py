num1=int(input("enter the number"))
num2=int(input("enter the number"))
sum1,sum2=0,0
for i in range(1,num1+1):
    if(num1%i==0):
        sum1+=i
for j in range(1,num2+1):
    if(num2%j==0):
        sum2+=j
if (sum1/num1) == (sum2/num2):
    print("friendly number")
else:
    print("not a friendly number")    
