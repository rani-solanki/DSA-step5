import sys
def secondmax(list,n):
    max2 = 0
    max = 0
    for j in range(len(list)-1):
        if (max < list[j+1]):
            max = list[j+1]
        if (list[j] < list[j+1]< max):
            max2 = list[j+1]
    print(max2)

def secondmin(list,n):
    if n < 2:
        print("minmun size of two")
        pass
    if n == 2:
        if list[0]==list[1]:
            print("both are no equal to each other")   
    Min = sys.maxsize
    sec_min = sys.maxsize
    for i in range(0,n):
        if list[i] < Min:
            sec_min=Min
            Min=list[i]
        elif list[i]> Min and list[i]<sec_min:
            sec_min = list[i]
    if (sec_min == sys.maxsize):
        print("no seconmin no ")
    else:
        print("the secondmin no is  ",sec_min)

list = [2,90,3,0,23,-2,45,-1]
n=len(list)
secondmax(list,n)
secondmin(list,n)




