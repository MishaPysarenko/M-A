
#include <iostream>

struct ListNode
{
    int val;
    ListNode* next;

    ListNode(int x, ListNode* n = nullptr)
        : val(x), next(n) {}
};

ListNode* swapPairs(ListNode* head)
{
    if (head == nullptr || head->next == nullptr)
        return head;

    ListNode* second = head->next;

    head->next = swapPairs(second->next);
    second->next = head;

    return second;
}

void printList(ListNode* head)
{
    if (head == nullptr)
        return;

    std::cout << head->val << " ";
    printList(head->next);
}

int main()
{
    ListNode n4(4);
    ListNode n3(3, &n4);
    ListNode n2(2, &n3);
    ListNode n1(1, &n2);

    ListNode* head = swapPairs(&n1);

    printList(head); // 2 1 4 3
    return 0;
}
