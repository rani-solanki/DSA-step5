class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(A):
        strList = [1]

        if (A == 1):
            return "1"

        if (A == 2):
            return "11"
            
        for i in range(A-1):
            c = 1
            list = [ ]
            
            for j in range(len(strList)):
                if (j == len(strList)-1):
                    list.append(c)
                    list.append(strList[j])
                    break 
                if (strList[j] == strList[j+1]):
                    c +=1
                else:
                    list.append(c)
                    list.append(strList[j])
                    c = 1
            strList = list
        return "".join([str(x) for x in strList])
    num = int(input("enter the numver"))
    print(countAndSay(num))
        
        