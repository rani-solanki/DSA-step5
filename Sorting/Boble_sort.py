def bobbleSort(arr,arrSize):
    
    i=0
    while(i<arrSize):
        j=0
        while(j<arrSize):
            if (arr[i]<arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j]=temp
            j=j+1
        i=i+1    
    return arr
arrSize =int (input("enter the size of array"))
arr =[int(input(" enter the elements of array")) for each in range(arrSize)]
print(arr)

print(bobbleSort(arr,arrSize))

