
class MyCircularDeque:
    def __init__(self, k):
        self.data = [0] * k
        self.capacity = k
        self.front = 0
        self.size = 0

    def insertFront(self, value):
        if self.isFull():
            return False

        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False

        index = (self.front + self.size) % self.capacity
        self.data[index] = value
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False

        self.size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1

        index = (self.front + self.size - 1) % self.capacity
        return self.data[index]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


# Приклад
dq = MyCircularDeque(3)

print(dq.insertLast(1))   # True
print(dq.insertLast(2))   # True
print(dq.insertFront(3))  # True
print(dq.insertFront(4))  # False
print(dq.getRear())       # 2
print(dq.isFull())        # True
print(dq.deleteLast())    # True
print(dq.insertFront(4))  # True
print(dq.getFront())      # 4
