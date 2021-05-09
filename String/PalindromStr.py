# check whether string is palindrom or not

def isPalindrom(string,length):
    n = length -1
    result = False

    for i in range(length//2):
        E = n - i
        if(string[i] == string[E]): 
            result =  True

    if (result == True):
        return string, ": It is palindrome string"
    else:
        return string, ": It is not palindrom string"


string = input("enter the sentence")
length = len(string)
print(isPalindrom(string,length))


