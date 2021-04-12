def coverPoints(A, B):
    x = A[0]
    y = B[0]
    total = 0
    for cur1, cur2 in (A,B):
        dx = abs(cur1 - x)
        dy = abs(cur2 - y)
        
        if dx < dy:
            total += dy
        else:
            total += dx
        x, y = cur1,cur2
    return total

A = [4,10]
B = [10,12]
print(coverPoints(A,B))



