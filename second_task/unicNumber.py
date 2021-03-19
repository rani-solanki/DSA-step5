def unicElement(list,list2):
    
    print("unic element in both array")    
    i=0
    while(i<len(list)):
        if (list[i] in list2):
            
            print(list[i])
        i=i+1

def intersection(list,list2):
    unicNumber = []
    for i in list:
        if (i not in unicNumber):
            unicNumber.append(i)
    for j in list2:
        if (j not in unicNumber):
            unicNumber.append(j)

        return "instersection array ", unicNumber
list = [2,3,45,4,5,-1,56]
list2 = [45,6,2,-1,56]
unicElement(list,list2)

print(intersection(list,list2))









