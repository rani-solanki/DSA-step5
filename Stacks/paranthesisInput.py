def printParenthesis(str, n):
    if(n > 0):
        Parenthesis(str, 0,n, 0, 0)
        
def Parenthesis(str, pos, n,open, close):

    if(close == n):
        for i in str:
            print(i, end = "")
        print()

    else:
        if(open > close):
            str[pos] = '}'
            Parenthesis(str, pos + 1, n,
                              open, close + 1)
        if(open < n):
            str[pos] = '{'
            Parenthesis(str, pos + 1, n,
                              open + 1, close)
n = int(input("enter the number"))
strArray  = [""] * 2 * n
printParenthesis(strArray, n)









