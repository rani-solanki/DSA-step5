# find the string is isvalid or not opretors
test_good = 'L5L5L5'
def check_string(test):
    if test[0::2].isalpha() and test[1::2].isdecimal():
        return 'valid'
    else:
        return 'Invalid'
        
print(check_string(test_good))
# confirm the string is valid or not using the opretors nd oprends 

def isValid(string,n):
    sublen = n//2
    k=0
    # create new list 
    operands = [""] * sublen 
    operators = [""] * (n -sublen)

    ans1 = 0; ans2 = 0; ans3 = 0; 
    for i in range(len(string)):
        if (string[i] != '+' and string[i] != '=' and string[i] != '-' and string[i] != '*' and string[i]!='/'):
            operands[k] += string[i]; 
        else: 
            operators[k] = string[i]

            if (k == 1) : 
                if (operators[k-1] == '+') : 
                    ans1 += int(operands[k -1]) + int(operands[k]); 
    
                if (operators[k-1] == '-') :
                    ans1 += int(operands[k]) - int(operands[k]); 
            if (k == 2):
                if (operators[k-1] == '+') :
                    ans2 += ans1 + int(operands[k]); 
    
                if (operators[k-1] == '-') :
                    ans2 -= ans1 - int(operands[k]); 

            if (k == 3):
                if (operators[k - 1] == '+') :
                    ans3 += ans2 + int(operands[k])
    
                if (operators[k - 1] == '-') :
                    ans3 -= ans2 - int(operands[k])
            k=k+1

    if (ans3 == int(operands[4])) :
        return 'Valid'
    else :
        return 'Invalid'

string = input( "enter the string not present letter")
n = len(string)
print(isValid(string , n))




