#find the sum of squares of a digit in agiven number
n=int(input())
rem,sum=0,0
while(n>0):
    rem=n%10
    sum+=(rem**2)
    n=n//10
print(sum)    
