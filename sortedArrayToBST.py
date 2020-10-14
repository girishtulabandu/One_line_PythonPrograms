
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def sortedArraytoBST(arr):

    if not arr:
        return None

    mid = (len(arr))//2

    root = Node(arr[mid])

    root.left = sortedArraytoBST(arr[:mid])
    root.right = sortedArraytoBST(arr[mid+1:])

    return root

def preOrder(node):
    if not node:
        return

    print(node.data)
    preOrder(node.left)
    preOrder(node.right)

'''
arr = [1, 2, 3, 4, 5, 6, 7] 
root = sortedArraytoBST(arr)
print("\n")
print("PreOrder Traversal of constructed BST from sorted array: "), 
preOrder(root) 
'''
