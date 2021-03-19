# Find an element in a given matrix such that each row and each column is sorted.

def Findnumber(list,Size,n):
    i=0
    
    positionlist = []
    while(i< Size):
        j=0
        while(j<len(list[i])):
            if(list[i][j] == n ):
                a = i,j
                positionlist.append(a)
            j=j+1
        i=i+1

    if (positionlist != []):

        return positionlist
    else:
        return "n is not present in list"

    return positionlist

list = [ [11, 21, 31, 41, 51 ],
    [12, 22, 32, 42, 52 ],
    [13, 23, 33, 43, 53 ],
    [14, 24, 34, 44, 54 ],
    [15, 25, 35, 45, 55 ] ]

Size = len(list)
n = int(input("enter the number"))

print(Findnumber(list ,Size, n))

