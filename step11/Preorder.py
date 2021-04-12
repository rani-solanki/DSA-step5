class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def PreOrder(self):

        print(self.val, end=' ')

        if self.left:
            self.left.PreOrder()

        if self.right:
            self.right.PreOrder()

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    print("Pre order Traversal")
    root.PreOrder()
    print(" ****** ")
   

