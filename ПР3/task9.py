
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head, x):
    less = ListNode()
    greater = ListNode()

    left = less
    right = greater

    while head:
        if head.val < x:
            left.next = head
            left = left.next
        else:
            right.next = head
            right = right.next

        head = head.next

    right.next = None
    left.next = greater.next

    return less.next


# Приклад 1
head = ListNode(1, ListNode(4,
       ListNode(3, ListNode(2,
       ListNode(5, ListNode(2))))))

result = partition(head, 3)

while result:
    print(result.val, end=" ")
    result = result.next
# Output: 1 2 2 4 3 5

print()

# Приклад 2
head = ListNode(2, ListNode(1))
result = partition(head, 2)

while result:
    print(result.val, end=" ")
    result = result.next
# Output: 1 2
