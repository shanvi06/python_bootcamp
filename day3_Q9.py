#find the element that is present in k+N th index
#k is given by user-3
#N=2
#3 6 8 4 61 2
#output=2

#k=3
#n=4
#80 70 54 36 72
#output-error

k=int(input())
n=int(input())
list=list(map(int,input().split()))
if len(list) < (k+n):
    print("error")
else:
    for i in range(len(list)):
        print(list[k+n])
        break
        




    

