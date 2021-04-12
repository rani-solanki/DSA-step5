#  Inorder (Left, Root, Right) : 5 2 6 1 3 
# first I have to create node 

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val= key

def isEmpty():
    stack = []
    return stack


def Inorder(root):
    curr = root
    stack = isEmpty()

    while not False:
        while curr != None:
            stack.append(curr)
            curr = curr.left

        if(stack):

            curr = stack.pop()
            print(curr.val, end=" ")

            curr = curr.right

        else:
            break

    print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)
root.left.right = Node(6)

Inorder(root)

