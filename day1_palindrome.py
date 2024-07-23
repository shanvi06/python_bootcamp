
s=input("enter the string")
p=""
for i in s:
    p=i+p
if(p==s):
    print("palindrome")
else:
    print("not palindrome")        