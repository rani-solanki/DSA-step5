def Factorial(n):

    if n == 0:
        return 1
      
    return n * Factorial(n-1)
   
num = int(input("enter the number"))

if(num<0):
    print(" dose't exit the negative number")
if (num > 1):
    print("factorial of this", num,":",Factorial(num))
   
