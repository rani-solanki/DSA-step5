def rightShift(list,user):
    leftShift=[]
    leftShift = list.copy()
    i=0
    while(i < user):
        leftShift.append(list[0])
        leftShift.remove(list[0])
        i=i+1

    print(leftShift)

def leftShift(list1,user1):
    j=1
    while(j <= user1):
        list1.insert(0,list1[-1] )
        list1.pop()
        j=j+1
    print(list1)
    
list = [2,3,1,3,4,5,7,9,4]
user = int(input("enter the number"))
list.reverse()
print(list)
rightShift(list,user)
leftShift(list,user)


















