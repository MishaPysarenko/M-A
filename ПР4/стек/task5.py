
def decodeString(s):
    stack = []
    current = ""
    number = 0

    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)

        elif char == '[':
            stack.append((current, number))
            current = ""
            number = 0

        elif char == ']':
            previous, count = stack.pop()
            current = previous + current * count

        else:
            current += char

    return current


print(decodeString("3[a]2[bc]"))
# aaabcbc

print(decodeString("3[a2[c]]"))
# accaccacc

print(decodeString("2[abc]3[cd]ef"))
# abcabccdcdcdef
