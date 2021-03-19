def Compairetion(list,sum):

    list.sort()
    print(list)
    index = len(list)-1
    newNum = 0
    while(newNum < index):
        if (list[newNum] + list[index] == sum):
            print("it is equal to sum =:",list[newNum],list[index])
        if (list[newNum] + list[index]<sum):
            newNum = newNum+1
        else:
            index = index-1

list = [2,1,3,4,5,9,0]
n = len(list)
sum = int(input("entre the number"))
Compairetion(list,sum)




