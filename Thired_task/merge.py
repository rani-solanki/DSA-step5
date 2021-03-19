def MergeArrays(list1,list2):
    list = [ ]
    i=0
    j=0
    while(i<len(list1) and j < len(list2)):
        if list1[i] < list2[j]:
            list.append(list1[i])
            i=i+1
        elif list1[i]>list2[j]:
            list.append(list2[j])
            j=j+1
        else: 
            list.append(list1[i])
            i=i+1
            j=j+1

    while(i < len(list1)):
        list.append(list[i])
        i=i+1

    while(j < len(list2)):
        list.append(list2[j])
        j=j+1
    return list

list1 = [2,3,4,5]
list2 = [1,7,8,9]
print(MergeArrays(list1,list2))









