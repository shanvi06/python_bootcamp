#GCD of two numbers 
#Euclidean algorithm
a=int(input())
b=int(input())
while(b):
    a,b=b,a%b
print(a)    