def findMin(v,Note):

    cons = []
    n=len(Note)
    i = n - 1
    while(i >= 0):
        while (v >= Note[i]):
            v =v- Note[i]
            print(v)
            cons.append(Note[i])

        i -= 1
    return cons

n = int(input("enter the number"))
deno = [1, 2, 5, 10, 20, 50,100, 500, 1000,2000]
print("noOfCons",findMin(n , deno))

	