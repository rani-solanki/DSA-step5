def DuplicateNumber(arr,arrSize):
    if (arrSize > 2):
        print("size should be less than two")
        list = []
        list2 = []
        for index in range(arrSize):
            if arr[index] not in list:
                list.append(arr[index])
            elif arr[index] not in list2:
                list2.append(arr[index])

        print(list2)
arr = [4,3,45,2,2,3,4,9]
arrSize  = len(arr)
DuplicateNumber(arr, arrSize)












