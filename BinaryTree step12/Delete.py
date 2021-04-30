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

def DeleteNode(root, key):
    parent = None
    New = root
    while New and New.data != key:
        parent = New
        if key < New.data:
            New = New.left
        else:
            New = New.right
    if New == None:
        return root
    if (New.left and New.right) == None:
        if New!= root:
            if parent.left == New:
                parent.left = None
            else:
                parent.right = None
        else:
            root = None
            
    elif New.left and New.right:
        successor = getMinimumKey(New.right)
        val = successor.data
        deleteNode(root, successor.data)
        New.data = val
    else:
        if New.left:
            child = New.left
        else:
            child = New.right
        if New != root:
            if New == parent.left:
                parent.left = child
            else:
                parent.right = child
        else:
            root = child
    return root

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
root = DeleteNode(root ,n)
print("deleted elment from the Bst",n)
if Search(root,n):
	print("Yes")
else:
	print("No")
