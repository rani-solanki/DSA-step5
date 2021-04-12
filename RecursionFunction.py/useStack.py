def isEmpty():
    stack = []
    return stack

def pop(stack):
    stack.pop()

def factorial(n):
    stack.append(n)
    if(n <= 1):
        return
    else:
        factorial(n-1)
        pop(stack)
        return stack

stack = isEmpty()
for i in range(4):
    n = int(input("enter the numebr"))
    print(factorial(n))








