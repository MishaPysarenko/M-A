
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        kth = group_prev

        for i in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next

        group_next = kth.next
        prev = group_next
        current = group_prev.next

        while current != group_next:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        temp = group_prev.next
        group_prev.next = kth
        group_prev = temp


# Приклад 1
head = ListNode(1, ListNode(2,
       ListNode(3, ListNode(4, ListNode(5)))))

result = reverseKGroup(head, 2)

while result:
    print(result.val, end=" ")
    result = result.next
# Output: 2 1 4 3 5

print()

# Приклад 2
head = ListNode(1, ListNode(2,
       ListNode(3, ListNode(4, ListNode(5)))))

result = reverseKGroup(head, 3)

while result:
    print(result.val, end=" ")
    result = result.next
# Output: 3 2 1 4 5
