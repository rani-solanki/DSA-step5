def multiple(M1,M2):
    # multiple of metrix 
    sum2 = 1
    sum = 1
    a = []
    b = []
    for i in range(len(M1)-1):
        for j in range(len(M2[i])-1):
            sum = sum * M1[i][j]
            sum2 = sum2 * M2[i][j]

    # program to multiply two
    # rectangular matrices

    for l in range(len(M1)):
        multiple = 1
        seco_multiple = 1
        for m in range(len(M2)):
            multiple = M1[0][m] * M1[1][m]
            seco_multiple = M2[0][m] * M2[1][m]

            a.append(multiple)
            b.append(seco_multiple)

    return a,b
M1 = [[1,2,3],[3,2,1]]
M2 = [[4,5,6],[6,5,4]]

print(multiple(M1,M2))







