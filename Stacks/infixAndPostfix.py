def isOperator(input):
    switch = {'+': 1, '-': 1,'*': 1,'/': 1,'%': 1, '(': 1}
    return switch.get(input, False)
    
def isOperand(input):  
    if ((ord(input) >= 65 and ord(input) <= 90) or
        (ord(input) >= 97 and ord(input) <= 122)):
        return 1
    return 0
def inPrec(input):

    switch = {'+': 2,'-': 2,'*': 4,'/': 4,'%': 4,'(': 0,}
    return switch.get(input, 0)

def outPrec(input):
    switch = {'+': 1,'-': 1,'*': 3,'/': 3,'%': 3,'(': 100,}
    return switch.get(input, 0)
    
def inToPost(input):
    i = 0
    s = []
    while (len(input) != i):
        if (isOperand(input[i]) == 1):
            print(input[i], end = "")
        elif (isOperator(input[i]) == 1):
            if (len(s) == 0 or 
                outPrec(input[i]) >
                 inPrec(s[-1])):
                s.append(input[i])
            else:
                while(len(s) > 0 and 
                      outPrec(input[i]) < 
                      inPrec(s[-1])):
                    print(s[-1], end = "")
                    s.pop()
                while(len(s) > 0 and 
                    s.append(input[i])
        elif (input[i] == ')'):
            while(s[-1] != '('):
                print(s[-1], end = "")
                s.pop()

                if(len(s) == 0):
                    print('Wrong input')
                    exit(1)
            s.pop()
        i += 1
    while(len(s) > 0):
        if(s[-1] == '('):
            print('Wrong input')
            exit(1)
              
        print(s[-1], end = "")
        s.pop()
input = "a+b*c-(d/e+f*g*h)"
  
print(inToPost(input))
  