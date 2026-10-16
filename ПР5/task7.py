
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minCameraCover(root):
    cameras = 0

    # 0 — вузол не покритий
    # 1 — на вузлі встановлена камера
    # 2 — вузол покритий камерою

    states = {}
    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()

        if node is None:
            continue

        if not visited:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
        else:
            left = states.get(node.left, 2)
            right = states.get(node.right, 2)

            if left == 0 or right == 0:
                cameras += 1
                states[node] = 1

            elif left == 1 or right == 1:
                states[node] = 2

            else:
                states[node] = 0

    if states[root] == 0:
        cameras += 1

    return cameras


# Приклад 1
root = TreeNode(
    0,
    TreeNode(0, TreeNode(0), TreeNode(0))
)

print(minCameraCover(root))
# 1


# Приклад 2
root = TreeNode(
    0,
    TreeNode(
        0,
        TreeNode(
            0,
            TreeNode(0, None, TreeNode(0))
        )
    )
)

print(minCameraCover(root))
# 2
