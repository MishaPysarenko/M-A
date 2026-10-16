
from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0


# Приклад
myStack = MyStack()

myStack.push(1)
myStack.push(2)

print(myStack.top())    # 2
print(myStack.pop())    # 2
print(myStack.empty())  # False
