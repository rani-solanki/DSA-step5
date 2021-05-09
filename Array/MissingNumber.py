def missNumber(arr,n): 
    result = 0
    for i in arr:
        if (i<0):
            result = False
            break
        else:
            result =    True

    if (result == True):
        n = n+1
        sumOfArray = sum(arr)
        pre = int( n*(n+1)/2) 
        print(pre - sumOfArray)
    else:
        print("negetive number is there")

NUm = int(input("enter the number"))
arr = [1, 2, 4, 6, 3, 7, 8]
n = len(arr)

missNumber(arr,n)



