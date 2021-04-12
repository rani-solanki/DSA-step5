def fibonancci(n):
    if (n == 0):
        return 0
        
    if (n == 1 ):
        return 1

    else:
        return (fibonancci(n - 1) + fibonancci(n - 2))
        
n = int(input("enter the number"))
if (n>0):
    for i in range(n):
        print(fibonancci (i))
else:
    print("not exit for the negative number")

    







