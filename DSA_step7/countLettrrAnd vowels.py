def Vowel(ch): 
    return ch.upper() in ['A', 'E', 'I', 'O', 'U'] 
    
# Returns count of vowels in str  
def countVowels(str): 
    count = 0
    for i in range(len(str)): 

        # Check for vowel 
        if Vowel(str[i]): 
            count += 1
    return count 

# Returns number of words in string
def countWords(string,length):
    state = True
    wc = 0 

    for i in range(len(string)):
 
        if (string[i] == ' ' or string[i] == '\n' or string[i] == '\t'):
            state = True
 
        elif state == True:
            state = False
            wc += 1

    return "words ",wc

# string object  

str = input('enter the sentence')
length = 0
for i in str:
    length = length+1

# Total number of Vowels 

print(countVowels(str))
print(countWords(str ,length))












