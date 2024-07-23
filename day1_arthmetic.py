""""
num1=int(input())
num2=int(input())
sum=(num1+num2)
sub=(num2-num1)
mul=(num1*num2)
div=(num1/num2)
pow=(num1**num2)
print(sum)
print(sub)
print(mul)
print(div)
print(pow)

age=int(input())
if(age>=18 and age<24):
    print("only two wheeler")
elif(age>=24 and age<45):
    print("two and four wheeler")
else:
    print("both")


apple=int(input())
banana=int(input())
orange=int(input())
cost1=(apple*15)
cost2=(banana*12*4)
cost3=(orange*5)
if(cost1+cost2+cost3)<=700:
    print("not cheated")
else:
    print("cheated")
""
s=int(input())
if(s>0 and s%2==0):
    print("positive even")
elif(s>0 and s%2!=0):
    print("positive odd")
elif(s<0 and s%2==0):
    print("negivtive even")
else:
    print("negitive odd")
"""

x_height=int(input())
x_weight=int(input())
y_height=int(input())
y_weight=int(input())
x_s,y_s=0,0
z_won=14*(50/100)
if(x_height==140 and x_weight%2==0):
    x_s==1
if((y_height>=118 or y_height<=148) and y_weight%z_won==0):
    y_s==1
if(x_s==1 and y_s==1):
    print("they will meet")
else:
    print("they will not meet")    
