class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def LeafCount(node):

	while node == None:
		return 0

	if (node.left and node.right) == None:
		return 1
        
	else:
		return LeafCount(node.left) + LeafCount(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


print ("leaf count ",LeafCount(root))

