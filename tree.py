class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        self.depth =-1


def depth(node):
    if not node:
        return 0
    else:
        if node.depth != -1:
            return node.depth
        else:
            return 1+max(depth(node.left),depth(node.right))



root = Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)

print root.depth


print depth(root.right)

