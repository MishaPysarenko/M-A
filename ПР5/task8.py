
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalTraversal(root):
    nodes = []
    stack = [(root, 0, 0)]

    while stack:
        node, row, col = stack.pop()

        if node is None:
            continue

        nodes.append((col, row, node.val))

        stack.append((node.left, row + 1, col - 1))
        stack.append((node.right, row + 1, col + 1))

    nodes.sort()

    result = []
    previous_col = None

    for col, row, value in nodes:
        if col != previous_col:
            result.append([])
            previous_col = col

        result[-1].append(value)

    return result


# Приклад 1
root = TreeNode(
    3,
    TreeNode(9),
    TreeNode(20, TreeNode(15), TreeNode(7))
)

print(verticalTraversal(root))
# [[9], [3, 15], [20], [7]]


# Приклад 2
root = TreeNode(
    1,
    TreeNode(2, TreeNode(4), TreeNode(5)),
    TreeNode(3, TreeNode(6), TreeNode(7))
)

print(verticalTraversal(root))
# [[4], [2], [1, 5, 6], [3], [7]]


# Приклад 3
root = TreeNode(
    1,
    TreeNode(2, TreeNode(4), TreeNode(6)),
    TreeNode(3, TreeNode(5), TreeNode(7))
)

print(verticalTraversal(root))
# [[4], [2], [1, 5, 6], [3], [7]]
