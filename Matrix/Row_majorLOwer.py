# Lower and upper Triangular Matrix Row-Major Mapping
# Function to form lower triangular marix
def lower(matrix, row, col):	
	for i in range(0, col):
		for j in range(0, row):
			if (i < j):
				print("0", end = " ")
			else:
				print(matrix[i][j], end = " " )
		print(" ")
	
# Function to form upper triangular marix
def upper(matrix, row, col):
	for i in range(0, col):
		for j in range(0, row):
			if (i > j):
				print("0", end = " ")
			else:
				print(matrix[i][j],end = " " )
		print(" ")


def RowMajor(array,col,row):    
    rowMajor = []
    i=0
    j = 0
    while(i<col):
        subArray = []
        m = 0
        while(m<row):
            subArray.append(array[j])
            j=j+1
            m=m+1
        i=i+1
        rowMajor.append(subArray)

    return rowMajor

array = [2,3,1,2,3,6,5,4,3,2,32,45]

row = int(input("row :"))
col = int(input("colum :"))

matrix = RowMajor(array,col,row)
print(matrix)

print("Lower triangular matrix: ")
lower(matrix, row, col)

print("Upper triangular matrix: ")
upper(matrix, row, col)


