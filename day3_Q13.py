#replace the elements in an array with average of max and min element
list=list(map(int,input().split()))
max,min=list[0],list[0]
avg=0
for i in list:
    if i>max:
        max=i
for j in list:
        if j<min:      
            min=j
avg=(max+min)//2            
for i in range(len(list)):
    list[i]=avg
print(list)