
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


# Приклад 1
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

print(hasCycle(head))  # True

# Приклад 2
head = ListNode(1, ListNode(2))
head.next.next = head

print(hasCycle(head))  # True

# Приклад 3
head = ListNode(1)

print(hasCycle(head))  # False
