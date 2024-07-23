#print("Hello Swec")

#var1 = "Shanvi"
#print("Good Morning,",var1)

#name=input("enter your name\n")
#print(name)

#age,name=20,"Shaanvi"
#name="Shaanvi"
#print(f"Hello {name}, you are {age} years old")

#name=input("enter your name")
#n=int(input("enter the no of subjects"))
#n1=int(input("enter the marks"))
#n2=int(input("enter the marks"))
#n3=int(input("enter the marks"))
#sum,avg=0,0
#sum=n1+n2+n3
#avg=(sum/n)
#print(f"Hello {name}\n Your total marks are {sum}\n Average is {avg}")

name=input()
age=int(input())
if age <= 18:
    print(f"{name}, you are not eligible for voting")
else:
    print(f"{name},as you are {age}, you are eligible for voting") 
