# check whether both string is anagram or not?

def AnagramStr(str1,str2,f1,f2):
    # sorted the array
    str1 = sorted(str1) 
    str2 = sorted(str2) 

    # itrets the element 
    result = 1
    for i in range(len(str1) or len(str2)):
        if (str1[i] == str2[i]):
            result = 0

    # check wether both str in anagram or not
    if (result == 1):
        return "it is not anagram to each other"
    else:
        return "it is anagramStr to each other"

# given the two string from user input
str1 = input("enter the a word")
str2 = input("enter the a word")

# find the len of the both string f1 and f2
f1 =  len(str1)
f2 = len(str2)
print(AnagramStr(str1,str2,f1,f2))




