def binarySearch(arr,low,length, num):

    if (length >= low):
        mid = (length+low)//2

        if (arr[mid] == num):
            return mid
        elif(arr[mid] > num):
            return binarySearch(arr,num,mid-1,low)
        else:
            return binarySearch(arr,num,length,mid+1)
    return -1

arr = [2,3,1,2,4,567,34]
num = int(input("enter the number"))
length = len(arr)
result = binarySearch(arr,0,length-1,num)
if result != -1:
    print(num, "element is present in the array")
else:
    print(num,"element is not present is the array")

