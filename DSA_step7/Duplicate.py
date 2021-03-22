# find the dulicate element in string 

def duplicate(string,n):

    # take the empty list
    list = []
    i=0
    for j in range(n):
        if (string[j] not in list):
            list.append(string[j])
        elif list[j-i] in string:
            print(string[i])
        i=i+1

    print(list)

# take a string from the user
string = input("enter the sentence")
n = len(string)
duplicate(string, n)









