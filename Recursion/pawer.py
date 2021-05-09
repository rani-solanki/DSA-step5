def power(n,x):
    if (x == 0):
        return 1
    else:
        return (n*power(n , x-1))
    
n = int(input("enter the number"))
x = int(input("enter the number"))
print(power(n,x))









