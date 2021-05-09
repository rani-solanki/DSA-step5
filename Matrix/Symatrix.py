def transpose(mat, tr, N):
	for i in range(N):
		for j in range(N):
			tr[i][j] = mat[j][i]

def isSymmetric(mat, N):
	
	tr = [ [0 for j in range(len(mat[0])) ] for i in range(len(mat)) ]
	transpose(mat, tr, N)
	for i in range(N):
		for j in range(N):
			if (mat[i][j] != tr[i][j]):
				return False
	return True

mat = [ [ 1, 3, 5 ], [ 3, 2, 4 ], [ 5, 4, 1 ] ]

print (True if (isSymmetric(mat, 3)) else False)
