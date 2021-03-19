def SelectionSort(array,SizeArray):
    # sort the array
    i=0
    while(i<SizeArray):
        min = 0
        j=i+1
        while(j<SizeArray):
            if (array[i] > array[j]):
                # swap the min element to next elemnt

                min = array[j]
                array[j] = array[i]
                array[i] = min

            j=j+1
        i=i+1
    return print("Sorted array ",array)
SizeArray = int(input("entre the Array size"))
array = [int(input("enter the number")) for i in range(SizeArray)]
print( "UNsorted array ",array)
print(SelectionSort(array,SizeArray))


