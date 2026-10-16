
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    if list1 is None:
        return list2

    if list2 is None:
        return list1

    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2


# Приклад 1
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

result = mergeTwoLists(list1, list2)

while result:
    print(result.val, end=" ")
    result = result.next

# Output: 1 1 2 3 4 4
