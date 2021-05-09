class Node:
    left = right = None
    def __init__(self, data):
        self.data = data

def isEmpty():
    stack = []
    return stack

def Order(root):
    order = []
    if root:
        Order(root.right)
        Order.append(root.data)
        print(Order)
        Order(root.left)
    else:
        return
        
def insert(root,key):
    if root == None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

stack = isEmpty()
keys = int(input("enter the number"))
for i in range(keys):
    node = int(input("enter the number"))
    stack.append(node)
    
print(stack)
root = None
for key in stack:
    root = insert(root, key)
inorder(root)
 
