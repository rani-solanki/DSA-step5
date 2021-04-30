def Union(arr1, arr2, m, n):
    i, j = 0, 0   
    union = []
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            union.append(arr2[j])
            j+= 1
        else:
            union.append(arr2[j])
            j += 1
            i += 1

    while i < m:
        union.append(arr1[i])
        i += 1
  
    while j < n:
        union.append(arr2[j])
        j += 1
    return union
    
def isinsertion(arr1,arr2, m,n):
    for i in range(0,n):
        if arr2[i] in arr1:
           print(arr2[i])
        elif(arr1[i] in arr2):
            print(arr1[i])

arr1 = [1, 2,7,0,45, 5, 6]
arr2 = [2,0,3, 5, 7]
m = len(arr1)
n = len(arr2)
print(Union(arr1, arr2, m, n))
isinsertion(arr1,arr2, m,n)
