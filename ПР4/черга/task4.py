
class MyCircularQueue:
    def __init__(self, k):
        self.data = [0] * k
        self.capacity = k
        self.front = 0
        self.size = 0

    def enQueue(self, value):
        if self.isFull():
            return False

        index = (self.front + self.size) % self.capacity
        self.data[index] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1

        return self.data[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1

        index = (self.front + self.size - 1) % self.capacity
        return self.data[index]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


# Приклад
myQueue = MyCircularQueue(3)

print(myQueue.enQueue(1))  # True
print(myQueue.enQueue(2))  # True
print(myQueue.enQueue(3))  # True
print(myQueue.enQueue(4))  # False
print(myQueue.Rear())      # 3
print(myQueue.isFull())    # True
print(myQueue.deQueue())   # True
print(myQueue.enQueue(4))  # True
print(myQueue.Rear())      # 4
