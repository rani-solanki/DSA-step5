def AddMetrix(M1,M2,M3,matrix_length):
    #To Add M1 and M2 matrices

    for i in range(len(M1)):
        for k in range(len(M2)):
            M3[i][k] = M1[i][k] + M2[i][k]

    return "The sum of Matrix M1 and M2 = ", M3
M1 = [[8, 14, -6],[12,7,4],[-11,3,21]]
M2 = [[3, 16, -6],[9,7,-4],[-1,3,13]]
M3  = [[0,0,0],[0,0,0],[0,0,0]]

matrix_length = len(M1)
print (AddMetrix(M1, M2, M3, matrix_length))



