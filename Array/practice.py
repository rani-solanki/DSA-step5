def removeDuplicates(list):
        # list = list.sort()
        i = 0
        deplicat = []
        for i in range(len(list)):
            if (list[i] not in deplicat):
                deplicat.append(list[i])
                
        return deplicat
list = [2,3,4,2,3,7,8,9]

print(removeDuplicates(list))

