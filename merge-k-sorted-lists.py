# Definition for singly-linked list.
# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nead = ListNode()
        current = nead

        while current:
            pass

        return ListNode()


    def min_index(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass

solution = Solution()
# x = solution.int_to_list(123)
# pass
x1 = ListNode(1, ListNode(4, ListNode(5)))
x2 = ListNode(1, ListNode(3, ListNode(4)))
x3 = ListNode(2, ListNode(6))
z = solution.mergeKLists([x1, x2, x3])
print(z)
