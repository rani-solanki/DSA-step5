class newNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def Search(root, key):
	while root is not None:
		if key > root.data:
			root = root.right
		elif key < root.data:
			root = root.left
		else:
			return True
	return False

def insert(Node, key):
	while Node == None:
		return newNode(key)

	if key < Node.data:
		Node.left = insert(Node.left, key)
	elif key > Node.data:
		Node.right = insert(Node.right, key)

	return Node

Bt = [23,43,51,15,67,65]
print(Bt)

root = None
for key in Bt:
    root = insert(root, key)

n = int(input("enter the number"))
if Search(root,n):
	print("Yes")
else:
	print("No")

