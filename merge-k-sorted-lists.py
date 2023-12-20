# Definition for singly-linked list.
# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        values = []
        x = self
        while x:
            values.append(x.val)
            x = x.next
        return str(values)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        while any(lists):
            x = [(index, value.val) for index, value in enumerate(lists) if value is not None]
            min_value = min(x, key=lambda item: item[1])[0]
            current.next = lists[min_value]
            current = current.next
            lists[min_value] = lists[min_value].next

        return head.next


    def mergeKLists_fast(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = tmp = ListNode()
        arr = []

        for l in lists:
            while l != None:
                arr.append(l.val)
                l = l.next

        for val in sorted(arr):
            tmp.next = ListNode()
            tmp = tmp.next
            tmp.val = val

        return head.next

solution = Solution()
# x = solution.int_to_list(123)
# pass
x1 = ListNode(1, ListNode(4, ListNode(5)))
x2 = ListNode(1, ListNode(3, ListNode(4)))
x3 = ListNode(2, ListNode(6))
z = solution.mergeKLists_fast([x1, x2, x3])
print(z)
