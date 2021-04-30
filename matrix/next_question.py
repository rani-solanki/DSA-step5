# uppercase to 1d array 

def UtrigleMETRIx(metrix,Arr,row):
    for i in range(row):
        for j in range(len(metrix[i])):
            if (metrix[i][j] !=0):
                Arr.append(metrix[i][j])

    return Arr

metrix = [[1, 2, 3, 4],
            [0, 5, 6, 7],
            [0, 0, 8, 9],
            [0, 0, 0, 10]]

Arr = [ ]
row = len(metrix)
print(UtrigleMETRIx(metrix,Arr,row))








