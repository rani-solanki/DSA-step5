# find the reverse of string

def ReverseStr (str,length):
    n= length -1 
    for i in range(length//2):

        temp = str[i]
        str[i] = str[n]
        str[n] = temp
        n = n-1
        i=i+1
    return str

# string give by user
string = input("enter the sentence")
if (len(string) == 1):
    str = string.split(" ")
else:
    str = list(string)

length = len(str)
print(ReverseStr(str,length))



