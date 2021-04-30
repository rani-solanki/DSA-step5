def twoSum(List, target: int):
    size = len(List)
    if (size == 0):
        return []
    if (size == 2 and List[0]+list[1] == target):
        return [0,1]
    arr = []
    for i in range(0,size):
        for j in range(i+1,size):
            if(List[i]+List[j]==target):
                a = [i,j]
                arr.append(a)
    return arr
List = [1,3,2,4,5,1]
target = 6
print(twoSum(List, target))
    
                   