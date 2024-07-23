#find even or odd
#find greatest of three
#find sum of all elements in an array
#find peak element in an array
#find max element
#find second max element in an array
#reverse an array without using builtin functions
#find the sum of squares of given number
#find sum of squares of even and odd digits
#check whether given number is palindrome or not(using while)
#write a program to print first n fibonacci series
''''
#even and odd
list=list(map(int,input().split()))
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)    
print(even,odd)        
'''

#peak element
list=list(map(int,input().split()))
count=0
for i in range(1,len(list)-1):
    if list[(i)] > list[i-1] and list[(i)] > list[(i+1)]:
        count=i
if(list[-1]>list[-2] and list[-1]>count):
    count=len(list)-1
print(list[count])    
   


''' 
#palindrome
n=int(input())
s=n
rev=""
while(n>0):
    rem=n%10
    rev+=str(rem)
    n=n//10
if s==int(rev):
    print("palindrome")
else:
    print("not palindrome")        

    

n=int(input())
prev=0
pres=1
count=0
while(count<n):
    print(prev)
    sum=prev+pres
    prev=pres
    pres=sum
    count+=1
    '''
    
    

    



  