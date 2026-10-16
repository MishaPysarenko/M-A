
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    if head is None or head.next is None:
        return head

    head.next = deleteDuplicates(head.next)

    if head.val == head.next.val:
        return head.next

    return head


# Приклад 1
head = ListNode(1, ListNode(1, ListNode(2)))
result = deleteDuplicates(head)

while result:
    print(result.val, end=" ")
    result = result.next
# Output: 1 2

print()

# Приклад 2
head = ListNode(1, ListNode(1, ListNode(2,
       ListNode(3, ListNode(3)))))

result = deleteDuplicates(head)

while result:
    print(result.val, end=" ")
    result = result.next
# Output: 1 2 3
