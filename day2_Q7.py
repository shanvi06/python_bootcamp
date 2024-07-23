"""
#7.1
#you are given with a (,) separated natural numbers 1 to 10. Print even numbers
list=list(map(int,input().split(",")))
for i in range(1,len(list),2):
        print(list[i],end=" ")


#7.2
#how many even numbers are there in above question
list=list(map(int,input().split(",")))
count=0
for i in range(1,len(list),2):
        count+=1
print(count)        


#7.3
#you are given with a space separated integer list find the number of even elements and number of odd elements in a given list
list=list(map(int,input().split(" ")))
even_count,odd_count=0,0
for i in list:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1   
print(even_count,odd_count)   
      



#7.4
#given an space separated integer list find the average of elements present in the even index
list=list(map(int,input().split(" ")))
sum,count=0,0
for i in range(0,len(list),2):
    sum+=list[i]
    count+=1
print(sum/count)    

"""


#7.5
#write a program to find area of a circle
#write a program to find perimeter of a circle
#write a program to find area of a triangle
#write a program to find perimeter of a triangle


