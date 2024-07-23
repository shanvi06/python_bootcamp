'''
#check how many vowels and consonants are there in a string
vow="aeiou"
con="bcdfghjklmnpqrstvwxyz"
inp=input()
count,flag=0,0
s=inp.lower()
for i in s:
    if i in vow:
        count+=1
for i in s:
        if i in con:        
            flag+=1
print(count,flag)



  #print all the vowels follwed by consonants without repeating
inp=input()
s=inp.lower()
vow="aeiou"
con="bcdfghjklmnpqrstvwxyz"
v=""
c=""
ans=""
for i in s:
    if i in vow:
        if i not in ans:
            ans+=i
for i in s:
    if i in con:
        if i not in ans:
            ans+=i
print(ans)         




#print the unique characters in a string
n=input()
a=n.lower()
s=""
for i in a:
    if i not in s:
        s+=i
print(s)        

#print the sum of the digits in the string
n=input()
sum=0
for i in n:
    if i.isdigit():
        sum+=int(i)
print(sum)

#sum of digits without using builtin functions
n=input()
s="0123456789"
sum=0
for i in n:
    if i in s:
        sum+=int(i)
print(sum)      



#reverse the numbers present in the given string
n=input()
s="0123456789"
ans=""
for i in n:
    if i in s:
        ans+=i
num=int(ans)    
a=""
while(num>0):
    rem=num%10
    a+=str(rem)
    num=num//10
print(int(a))    



n=input()
sum=0
for i in n:
    if (ord(i)>=ord('0') and ord(i)<=ord('9')):
        sum+=int(i)
print(sum)        



#print the capital letters present in the given string
n=input()
s=""
for i in n:
    if (ord(i)>=65 and ord(i)<=90):
        s+=i
print(s)        



#91,93,123,125,40,41

#remove all the brackets from the given algebraic expression
n=input()
for i in n:
    if ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125 or ord(i)==40 or ord(i)==41:
        pass
    else:
        print(i,end=" ")



n=input()
s=n.upper()
for i in s:
    print(chr(ord(i)+4),end=" ")
'''

n=input()
count=0
s=""
for i in n:
    if ord(i)==ord("-"):
        count+=1
    else:
        s+=i    
print("-"*count+s)