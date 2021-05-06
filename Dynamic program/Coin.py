# if N = 4 and S = [1,2,3] output should be come four like [1,1,1,1], [1,1,2],[2,2][3,1]

def count(arr, m, n ):
	if (n == 0):
		return 1

	if (n < 0):
		return 0

	if (m <= 0 and n >= 1):
		return 0
	return count( arr, m - 1, n ) + count( arr, m, n-arr[m-1] )

arr = [1,2,3]
N = len(arr)
num = int(input("enter the number"))
print(count(arr, N, num))

