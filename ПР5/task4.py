
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root, k):
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        k -= 1

        if k == 0:
            return current.val

        current = current.right

    return -1


# Приклад 1
root = TreeNode(
    3,
    TreeNode(1, None, TreeNode(2)),
    TreeNode(4)
)

print(kthSmallest(root, 1))
# 1


# Приклад 2
root = TreeNode(
    5,
    TreeNode(
        3,
        TreeNode(2, TreeNode(1)),
        TreeNode(4)
    ),
    TreeNode(6)
)

print(kthSmallest(root, 3))
# 3
