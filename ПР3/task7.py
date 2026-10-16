
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    current.next = list1 if list1 else list2
    return dummy.next


def mergeKLists(lists):
    if not lists:
        return None

    while len(lists) > 1:
        merged = []

        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(mergeTwoLists(list1, list2))

        lists = merged

    return lists[0]


# Приклад 1
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

result = mergeKLists([list1, list2, list3])

while result:
    print(result.val, end=" ")
    result = result.next
# Output: 1 1 2 3 4 4 5 6

print()

# Приклад 2
print(mergeKLists([]))  # None

# Приклад 3
print(mergeKLists([None]))  # None
