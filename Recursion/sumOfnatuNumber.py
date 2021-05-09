def Sum(n):
    if n <= 1:
        return n

    return n + Sum(n - 1)
  
n = int(input("enter the number"))
print(Sum(n))



