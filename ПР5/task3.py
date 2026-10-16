
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root


# Приклад 1
root = TreeNode(
    4,
    TreeNode(2, TreeNode(1), TreeNode(3)),
    TreeNode(7, TreeNode(6), TreeNode(9))
)

root = invertTree(root)
print(root.val, root.left.val, root.right.val)
# 4 7 2


# Приклад 2
root = TreeNode(2, TreeNode(1), TreeNode(3))

root = invertTree(root)
print(root.val, root.left.val, root.right.val)
# 2 3 1


# Приклад 3
root = None

print(invertTree(root))
# None
