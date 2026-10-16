
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recoverFromPreorder(traversal):
    stack = []
    i = 0
    n = len(traversal)

    while i < n:
        depth = 0

        while i < n and traversal[i] == '-':
            depth += 1
            i += 1

        value = 0

        while i < n and traversal[i].isdigit():
            value = value * 10 + int(traversal[i])
            i += 1

        node = TreeNode(value)

        while len(stack) > depth:
            stack.pop()

        if stack:
            parent = stack[-1]

            if parent.left is None:
                parent.left = node
            else:
                parent.right = node

        stack.append(node)

    return stack[0] if stack else None


# Допоміжна функція для виведення дерева
from collections import deque


def printTree(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node is None:
            result.append(None)
            continue

        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while result and result[-1] is None:
        result.pop()

    return result


# Приклад 1
root = recoverFromPreorder("1-2--3--4-5--6--7")
print(printTree(root))
# [1, 2, 5, 3, 4, 6, 7]


# Приклад 2
root = recoverFromPreorder("1-2--3---4-5--6---7")
print(printTree(root))
# [1, 2, 5, 3, None, 6, None, 4, None, 7]


# Приклад 3
root = recoverFromPreorder("1-401--349---90--88")
print(printTree(root))
# [1, 401, None, 349, 88, 90]
