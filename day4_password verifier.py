#password verifier
#Mr.X is trying to create a new password for his instagram account these are the required conditions for creating a new password
#Condition-1: min length is 8 and max length is 15
#Condition-2: only @,/ is allowed in a password
#Condition-3: no spaces are allowed
#Condition-4: only alpha numerics are allowed
#you are supposed to print 
#      weak if length is exact 8 
#      medium for length between 8-12 
#      strong for length between 12-15


password=input()
n=len(password)
count=0
new="@/"
if n<8 or n>15:
    print("Please follow the conditions")
else:
    for i in password:
        if (i in new[0] or new[1]) and " " not in password:
            count+=1
            break
    if count==0:
        print("follow the conditions")
    else:
        if n==8:
            print("Weak")
        elif n>8 or n<12:
            print("Medium")
        else:
            print("Strong")        
