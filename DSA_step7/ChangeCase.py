# Find the length and change cases 

def String(string):
    NewString = " "
    # if it is Tittle case 
    if (string.istitle()):
        c = string.lower()
        return c
        
    else:
        for i in string:
            if (i.isupper()):
                NewString = NewString + i.lower()
            elif(i.islower()):
                NewString = NewString + i.upper()
            else:
                NewString = NewString + " "
        return NewString

# Take the user input
string = input("entre the sentence")

# find the length of string
length  = 0
for chr in string:
    length = length+1

print(String(string))





