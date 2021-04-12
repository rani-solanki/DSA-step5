# Lower and upper Triangular Matrix Column-Major Mapping

def lOWECASE (n , metix,lowerCase,uppercase):

    for i in range(n):
        Llist = []
        ulist = []
        for j in range(n):
            if (i<j):
                Llist.append(0)
            if (i>j):
                ulist.append(0)
            else:
                ulist.append(metix[i][j])
                Llist.append (metix[i][j])

        lowerCase.append(Llist)
        uppercase.append(ulist)       

    print(lowerCase)
    print(uppercase)

metix =[[1,2,3],
        [2,3,4],
        [4,5,6]]

lowerCase = [ ]
uppercase = [ ]
length = len(metix)

lOWECASE(length, metix,lowerCase,uppercase)



