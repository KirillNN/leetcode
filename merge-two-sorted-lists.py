# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                current = current.next
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                current = current.next
                list2 = list2.next
        while list1 is not None:
            current.next = ListNode(list1.val)
            current = current.next
            list1 = list1.next
        while list2 is not None:
            current.next = ListNode(list2.val)
            current = current.next
            list2 = list2.next

        return head.next


solution = Solution()
# x = solution.int_to_list(123)
# pass
x = ListNode(1, ListNode(2, ListNode(4)))
y = ListNode(1, ListNode(3, ListNode(4)))
z = solution.mergeTwoLists(x, y)
print(z)
