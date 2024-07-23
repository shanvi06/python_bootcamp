#print the element in a particular index
index=int(input())
list=list(map(int,input().split()))
if index < len(list):
    print(list[index])
else:
    a=index%len(list)
    print(list[a])