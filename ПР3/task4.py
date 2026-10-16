
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head):
    if head is None or head.next is None:
        return

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None
    prev = None

    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    first = head
    second = prev

    while second:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2


# Приклад 1
head = ListNode(1, ListNode(2,
       ListNode(3, ListNode(4))))

reorderList(head)

while head:
    print(head.val, end=" ")
    head = head.next
# Output: 1 4 2 3

print()

# Приклад 2
head = ListNode(1, ListNode(2,
       ListNode(3, ListNode(4, ListNode(5)))))

reorderList(head)

while head:
    print(head.val, end=" ")
    head = head.next
# Output: 1 5 2 4 3
