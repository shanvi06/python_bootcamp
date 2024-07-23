
n=int(input("enter no"))
sqrt=int(n**0.5)
count=0
if(n<2):
    print("neither prime nor composite") 
elif n==2:
    print("prime")    
else:
    #for i in range(2,sqrt+1):  
    for i in range(2,(n//2)+1): 
        if(n%i==0):
            count+=1
            break
if(count==0):
    #if(count==0):   
    print("prime")
else:
    print("composite")   

"""
for(2,n//2)
if(count==1)
"""