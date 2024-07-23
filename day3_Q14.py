#find the missing number in an array(given sequence of numbers)
list=list(map(int,input().split()))
n=len(list)+1
sum=0
total_sum=n*(n+1)//2
for i in list:
    sum+=i
print(total_sum-sum)    