# find the minimum pranthesis bracket 
# find the leap of binary tree 
# find the similar element in strings
# find the length of string system like
# find the node one questions

def countnndSay(n):     
    # Base cases
    if (n == 1):
        return "1"
    if (n == 2):
        return "11"
       
    s = "11"
    for i in range(3, n + 1):
        s += '$'
        l = len(s)
        cnt = 1  
        tmp = ""     
        for j in range(1 , l):

            if (s[j] != s[j - 1]):
                tmp += str(cnt + 0)
                tmp += s[j - 1]
                cnt = 1

            else:
                cnt += 1
        s = tmp
    return s

N = int(input(("enter the number")))
print(countnndSay(N))
