# def getPairsCount(arr, n, sum,arr):
# 	count = 0 
# 	for i in range(0, n):
# 		for j in range(i + 1, n):
# 			if arr[i] + arr[j] == sum:
#                 list.append(i)
#                 list.append(j)
				
# 	return list

# arr = [1, 5, 7, -1, 5]
# n = len(arr)
# sum = 2
# list = []
# print("Count of pairs is",
# 	getPairsCount(arr, n, sum, list))

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
    
                   