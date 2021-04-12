def reverse(str):
    return("".join(reversed(str)))

def isEmpty():
    stack = []
    return stack

def pracidenci(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/' or operator == '%':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0

def inToprefix(stack, infixString,prefixS):
    i = 0
    while i in range(len(infixString)):
        if infixString[i].isalpha():
            prefixS += infixString[i]

        elif infixString[i] == ')' or infixString[i] == ']' or infixString[i] == '}':
            stack.append(infixString[i])

        elif infixString[i] == '(' or infixString[i] == '[' or infixString[i] == '{':

            if infixString[i] == '(' or '[' or '{':
                if stack[-1] != ')' or ']' or ']':
                    prefixS += stack.pop()
                stack.pop()
        else:
            if len(stack) == 0:
                stack.append(infixString[i])
            else:
                if pracidenci(infixString[i]) >= pracidenci(stack[-1]):
                    stack.extend(infixString[i])
                    
                elif pracidenci(infixString[i]) < pracidenci(stack[-1]):
                    prefixS += stack.pop()
                    p = len(stack) - 1

                    while p >= 0:
                        if (pracidenci(stack[p]) > pracidenci(infixString[i])):
                            prefixS += stack.pop()
                            p -= 1
                            if p < 0:
                                break
                    stack.extend(infixString[i])
                    
        i += 1
    while len(stack) != 0:
        prefixS += stack.pop()
    prefixS = reverse(prefixS)

    return prefixS
stack = isEmpty()
infix = input("enter the expresion:")
prefixS = ""
prefix = inToprefix(stack , infix,prefixS)
infix = reverse(infix)
print("postfix expresion: " + prefix)

