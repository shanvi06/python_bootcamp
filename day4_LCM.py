a=int(input())
b=int(input())
mul=a*b
while(b):
    a,b=b,a%b
print(mul//a)    