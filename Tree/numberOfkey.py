# find the node on which position 

class newNode:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def Level(root):
	while(root == 0):
		return
	q = []
	q.append([root, 1])
	p = []
	while (len(q)):
		p = q[0]
		q.pop(0)
		print("Level of", p[0].data, "is", p[1])

		if (p[0].left):
			q.append([p[0].left, p[1] + 1])
		if (p[0].right):
			q.append([p[0].right, p[1] + 1 ])

root = newNode(3)
root.left = newNode(2)
root.right = newNode(5)
root.left.left = newNode(1)
root.left.right = newNode(4)

Level(root)
