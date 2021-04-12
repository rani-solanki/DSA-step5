def isEmpty():
    quesue=[]
    return quesue
    
def enqueue(quesue,item, x):
    reap = -1
    frunt  = -1
    if (reap == x-1):
        print("over felow")

    elif (reap == -1 and frunt == -1):
        reap = frunt = 0
        quesue.append(n)
    else:
        reap+=1
        quesue.append(n)
    return quesue

def dequeue (quesue):
    frunt = reap = 0
    for i in range(len(quesue)-1):
        if (frunt == -1 and reap == -1):
            pass
        else:
            quesue.remove(quesue[frunt])
            frunt+=1
    return quesue

quesue = isEmpty()
x = int(input("enter the number"))
for each in range(x-1):
    n = int(input("enter the number"))
    print(enqueue (quesue, n,x))

print(dequeue (quesue))




