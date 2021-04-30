class Solution:
    # @param A : string
    # @return an integer

    def solve(A):
        size = len(A)
        if (A == " "):
            return -1
        if (A==1):
            if (A == "(" or ")" ):
                return 1
        if (A == ")(" ):
            return 2
            
        count = 0
        val = 0
        for i in range(size):
            if ( A[i] == "(" ):
                count +=1
            else:
                count+=-1
            if (count == -1):
                val+=1
                count+=1
                
        return count+val
    str = input("enter the parathesis")
    print(solve(str))