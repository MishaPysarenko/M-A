
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    if root is None:
        return []

    return (inorderTraversal(root.left) +
            [root.val] +
            inorderTraversal(root.right))


# Приклад 1
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(inorderTraversal(root))  # [1, 3, 2]

# Приклад 2
print(inorderTraversal(None))  # []

# Приклад 3
root = TreeNode(1)
print(inorderTraversal(root))  # [1]
