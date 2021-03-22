# solve the quick sort
def partition(list,lb,ub):
    pivoit = 0
    start = list[ub]
    end = list[lb]

    while(start<end):
        while(list[start]<=pivoit):
            start = start+1
        while(list[start] >= pivoit):
            end=end-1
        if (start < end):
            list[start],list[end] = list[end],list[start]
        
    list[lb],list[end] = list[end],list[lb]
    return end 

def quicksort(list , lb,ub):
    if (lb < ub):
        loc = partition(list, lb,ub)
        quicksort (list,lb,ub)
        quicksort (list,loc+1,ub)

list = [2,3,4,1,6,2,3]
lb = list[0]
ub = list[-1]
print(quicksort(list,lb,ub))

