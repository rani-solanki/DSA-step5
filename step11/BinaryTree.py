def factor(n) :
	res = 1
	for i in range(1, n + 1):
		res *= i
	return res
	
def bin(n, k):
	res = 1
	if (k > n - k):
		k = n - k
	for i in range(k):
		res *= (n - i)
		res //= (i + 1)
	return res

def catalan(n):
	c = bin(2 * n, n)
	return c // (n + 1)

def BST(n):
	count = catalan(n)
	return count

def BT(n):
	count = catalan(n)
	return count * factor(n)

n = int(input("enter the number"))
count1 = BST(n)
count2 = BT(n)
print("Count of BST with", n, "nodes is", count1)
print("Count of binary trees with", n, "nodes is", count2)
