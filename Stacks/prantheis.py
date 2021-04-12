def isEmpty():
    stack = []
    return stack
    
def BracketManage(stack,expr,brackets,arr):
    for char in expr:
        if char in brackets:
            stack.append(char)
        else:
            if stack == []:
                return False
            current_char = stack.pop()
            if current_char in brackets and char not in  arr:
                return False

    if stack==[]:
        return True
    return False

stack = isEmpty()
arr = ["(", "{", "["]
arr1 = [")","}","]"]
str = input("enter the number")
result = BracketManage(stack, str,arr,arr1)
if (result == True):
    print("balanced")
else:
    print("unbalaced")








 