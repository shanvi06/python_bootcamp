arr=list(map(int,input().split()))
n=len(arr)
arr.sort()
i=0
while(i<n//2):
    print(arr[i],end=" ")
    i+=1
j=n-1
while(j>=n//2):
    print(arr[j],end=" ")
    j-=1
    

