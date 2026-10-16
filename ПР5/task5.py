
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        if root is None:
            return ""

        result = []
        stack = [root]

        while stack:
            node = stack.pop()

            if node is None:
                result.append("null")
                continue

            result.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)

        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        values = iter(data.split(","))
        root = TreeNode(int(next(values)))
        stack = [(root, 0)]

        for value in values:
            while stack and stack[-1][1] == 2:
                stack.pop()

            node, state = stack[-1]
            child = None if value == "null" else TreeNode(int(value))

            if state == 0:
                node.left = child
            else:
                node.right = child

            stack[-1] = (node, state + 1)

            if child is not None:
                stack.append((child, 0))

        return root


# Приклад 1
root = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3, TreeNode(4), TreeNode(5))
)

codec = Codec()

data = codec.serialize(root)
print(data)
# 1,2,null,null,3,4,null,null,5,null,null

restored = codec.deserialize(data)

print(codec.serialize(restored))
# 1,2,null,null,3,4,null,null,5,null,null


# Приклад 2
root = None

data = codec.serialize(root)
restored = codec.deserialize(data)

print(restored)
# None
