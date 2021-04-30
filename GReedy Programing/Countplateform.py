def findPlatform(arr, dep, n):
	arr.sort()
	dep.sort()
	plat_needed = 1
	result = 1
	i = 1
	j = 0

	while (i < n and j < n):
		if (arr[i] <= dep[j]):
			plat_needed += 1
			i += 1
		else:
			plat_needed -= 1
			j += 1

		if (plat_needed > result):
			result = plat_needed
            
	return result

arr = [900, 9450, 950, 1100]
dep = [910, 1200, 1120, 113]
n = len(arr)

print("Minimum Number of Platforms Required = ",
	findPlatform(arr, dep, n))
