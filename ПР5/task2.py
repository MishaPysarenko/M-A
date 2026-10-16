
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    def isMirror(left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        return (
            isMirror(left.left, right.right)
            and isMirror(left.right, right.left)
        )

    if root is None:
        return True

    return isMirror(root.left, root.right)


# Приклад 1
root = TreeNode(
    1,
    TreeNode(2, TreeNode(3), TreeNode(4)),
    TreeNode(2, TreeNode(4), TreeNode(3))
)

print(isSymmetric(root))  # True


# Приклад 2
root = TreeNode(
    1,
    TreeNode(2, None, TreeNode(3)),
    TreeNode(2, None, TreeNode(3))
)

print(isSymmetric(root))  # False


# Приклад 3
root = TreeNode(
    1,
    TreeNode(2),
    TreeNode(1)
)

print(isSymmetric(root))  # False
