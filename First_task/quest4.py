list = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
low = 0
mid = 0
high = 0

i=0
while(i<len(list)):
    if (list[i] == 0):
        low = low+1
    elif (list[i] == 1):
        mid = mid+1
    else:
        high = high + 1
    i=i+1

# itret loop for low number
j=0
while (low>0):
    list[j]=0
    j+=1
    low = low-1
# itret loop for arrange the number
while (mid>0):
    list[j]=1
    j+=1
    mid = mid -1 
# itret loop for arrange the number
while (high>0):
    list[j]=2
    j+=1
    high = high -1

print (list)





    


