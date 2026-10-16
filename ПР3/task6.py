
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def doubleIt(head):
    if head.val >= 5:
        head = ListNode(0, head)

    current = head

    while current:
        current.val = (current.val * 2) % 10

        if current.next and current.next.val >= 5:
            current.val += 1

        current = current.next

    return head


# Приклад 1
head = ListNode(1, ListNode(8, ListNode(9)))
result = doubleIt(head)

while result:
    print(result.val, end=" ")
    result = result.next
# Output: 3 7 8

print()

# Приклад 2
head = ListNode(9, ListNode(9, ListNode(9)))
result = doubleIt(head)

while result:
    print(result.val, end=" ")
    result = result.next
# Output: 1 9 9 8
