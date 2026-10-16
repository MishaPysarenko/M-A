
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


# Приклад 1
head = ListNode(4, ListNode(5,
       ListNode(1, ListNode(9))))

deleteNode(head.next)

current = head
while current:
    print(current.val, end=" ")
    current = current.next
# Output: 4 1 9

print()

# Приклад 2
head = ListNode(4, ListNode(5,
       ListNode(1, ListNode(9))))

deleteNode(head.next.next)

current = head
while current:
    print(current.val, end=" ")
    current = current.next
# Output: 4 5 9
