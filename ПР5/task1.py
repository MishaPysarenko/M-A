
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val != q.val:
        return False

    return (
        isSameTree(p.left, q.left)
        and isSameTree(p.right, q.right)
    )


# Приклад 1
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))

print(isSameTree(p, q))  # True


# Приклад 2
p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(2))

print(isSameTree(p, q))  # False


# Приклад 3
p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))

print(isSameTree(p, q))  # False
