def Jumps(arr,MJA):
    Min=0
    l = len(arr)
    i=1
    while(i<l and i > Min):

        if Min+arr[Min] >= i:
            MJA.append(Min)
            i+=1
        else:
            Min+=1

    if MJA[-1]==0:
        return -1
    else:
        return MJA[len(MJA)-1]

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
MJA = []
print(Jumps(arr,MJA))





