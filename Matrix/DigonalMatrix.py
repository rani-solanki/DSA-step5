def Dailogfirst(metrix,n):
    firsDailo = [ ]
    secodDai = [ ]
    for i in range(n):
        for j in range(n):
            if (i == j):
               firsDailo.append(metrix[i][j])
            if (i+j == n-1):
                secodDai.append(metrix[i][j])

    return ("firsDailog",firsDailo), "secondDailog",secodDai

metrix = [
    [1,2,3,4],
    [4,3,2,1],
    [5,6,7,8],
    [8,7,6,5] ]

n = len(metrix)

print(Dailogfirst(metrix,n))
