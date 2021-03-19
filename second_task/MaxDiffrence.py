def FindMaxDiffrence(arr,MDiffrence):
    minElement = arr[0]

    i=0
    while(i < len(arr)):
        d = arr[i] - minElement
        if ( d > MDiffrence):
            MDiffrence = arr[i] - minElement
        if (arr[i] < minElement):
            minElement = arr[i]
        i=i+1
    return MDiffrence

arr = [2,5,3,4]
MDiffrence = arr[0] - arr[1]
print(FindMaxDiffrence(arr,MDiffrence))











