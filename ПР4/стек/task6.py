
def evalRPN(tokens):
    stack = []

    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            else:
                result = abs(a) // abs(b)
                if (a < 0) != (b < 0):
                    result = -result

            stack.append(result)
        else:
            stack.append(int(token))

    return stack[0]


print(evalRPN(["2", "1", "+", "3", "*"]))
# 9

print(evalRPN(["4", "13", "5", "/", "+"]))
# 6

print(evalRPN(["10", "6", "9", "3", "+", "-11",
               "*", "/", "*", "17", "+", "5", "+"]))
# 22
