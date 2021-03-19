# first method to find the duplicate Number
def Occrence(arr1, sizeOfArray):
    if (len(arr1 > 2)):
        arr1 = [ ]
        arr2 = [ ]
        for i in list:
            if (i not in arr1):
                arr1.append(i)
            elif (i not in arr2):
                arr2.append(i)

        return arr2
    else:
        print(arr1[0])

list = []
userNum = int(input("enter the number"))
list.append(userNum)
sizeOfArray = len(list)
print(Occrence(list,sizeOfArray))


# second method 
def DuplicateNUm(Nums):
    Nums.sort()
    for i in range(len(Nums)):
        if (Nums[i] == Nums[i-1]):
            print(Nums[i])
        else:
            pass


Array = [ ]
user = int(input("enter the number"))
for each in user:
    Array.append(user)
DuplicateNUm (Array)




