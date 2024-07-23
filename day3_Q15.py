#find the duplicates in an array
list=list(map(int,input().split()))
new_list=[]
dup=[]
for i in list:
    if (i in new_list):
        dup.append(i)
    else:
        new_list.append(i)      
print(dup)                 