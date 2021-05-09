class Node:
    def __init__(self, key):
        self.key = key

def Inorder(root):
    curr = root
    stack = []

    while not False:
        while curr != None:
            stack.append(curr)
            curr = curr.left

        if(stack):
            curr = stack.pop()
            print(curr.key, end=" ")
            curr = curr.right
        else:
            break
    print()

def BST(preorder, leftSide, rightSide):
    while leftSide > rightSide:
        return 

    node = Node(preorder[leftSide])
    i = leftSide
    
    while i <= rightSide:
        if preorder[i] > node.key:
            break
        i = i + 1

    node.left =  BST(preorder, leftSide + 1, i - 1)
    node.right = BST(preorder, i, rightSide)
    return node

preorder = [15, 10, 8, 12, 20, 16, 25]
root = BST(preorder, 0, len(preorder) - 1)
print("Inorder traversal of BST is ", end='')
Inorder(root)



