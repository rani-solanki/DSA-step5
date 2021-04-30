def minValue(A,B,n):

    A = sorted(A)
    B = sorted(B)
    print(A,B)
    result = 0
    for i in range(n) :
        result += (A[i] * B[n-1-i])
    return result
    
A = [6, 1, 9, 5, 4]
B = [3, 4, 8, 2, 4]
n = len(A)

print(minValue(A, B, n))
