def nCr(n, r):
    return (fact(n) / (fact(r) * fact(n - r)))

def fact(n):

    res = 1
    for i in range(2, n+1):
        res = res * i
    return res

num = int(input("enter the number"))
power = int(input("enter the number"))

print(int(nCr(num, power)))


