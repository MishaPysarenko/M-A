
def isValid(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()

    return len(stack) == 0


print(isValid("()"))      # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))      # False
