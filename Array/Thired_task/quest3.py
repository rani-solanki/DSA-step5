def Findnumber():
    i=0
    missNumber = [ ]
    while(i<len(list1)):
        if (list1[i] not in list2):
            missNumber.append(list1[i])
        i=i+1

    if (missNumber != list2):
        return "missNumber",missNumber


list1 = [6,7,4,3,5,6]
list2 = [2,1,4,5 ]

print(Findnumber())




        



