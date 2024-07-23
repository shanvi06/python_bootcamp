#write a program to print all the prime no's in a given range
m=int(input()) 
n=int(input())
for i in range(m,n+1): 
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,end=" ")