
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root):
    max_sum = float('-inf')
    stack = [(root, False)]
    gains = {}

    while stack:
        node, visited = stack.pop()

        if node is None:
            continue

        if not visited:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
        else:
            left = max(0, gains.get(node.left, 0))
            right = max(0, gains.get(node.right, 0))

            current_sum = node.val + left + right
            max_sum = max(max_sum, current_sum)

            gains[node] = node.val + max(left, right)

    return max_sum


# Приклад 1
root = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3)
)

print(maxPathSum(root))
# 6


# Приклад 2
root = TreeNode(
    -10,
    TreeNode(9),
    TreeNode(20, TreeNode(15), TreeNode(7))
)

print(maxPathSum(root))
# 42
