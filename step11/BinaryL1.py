# Binary Tree Traversal Easy Method 1

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def isEmpty():
    stack = []
    return stack

def height(node):
    if node is not None:
        lheight = height(node.left)
        rheight = height(node.right)
        
        while lheight > rheight :
            return lheight+1
        else:
            return rheight+1
    else:
        return 0

def Level(stack, root , level):
    while root is None:
        return
    if level == 1:
        a = root.data
        stack.append(a)

    elif level > 1 :
        Level(stack,root.left , level-1)
        Level(stack,root.right , level-1)

def LevelOrder(stack, root):

    h = height(root)
    for i in range(1, h+1):
        Level(stack, root, i)
    return stack

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
stack = isEmpty()
print("traversal of binary tree is -", LevelOrder(stack, root))


