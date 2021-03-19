def InsertArray(arr,arrSize):
    i=1
    while(i<arrSize:
        num = arr[i]
        j=i-1
        while( j >= 0) and num < arr[j]:
            arr[j + 1] = arr[j]
            j=j-1

        i=i+1
        arr[j + 1] = num
    print(arr)        
arrSize =int (input("enter the size of array"))
arr =[int(input(" enter the elements of array")) for each in range(arrSize)]
print(arr)
InsertArray(arr,arrSize)    








