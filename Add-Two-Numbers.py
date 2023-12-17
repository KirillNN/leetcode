# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.list_to_int(l1) + self.list_to_int(l2)

    def int_to_list(self, number: int) -> Optional[ListNode]:
        result = ListNode(number % 10)
        number//=10
        while number:
            result.next = ListNode(number%10)

    def list_to_int(self, l: Optional[ListNode]) -> int:
        result = 0
        step = 0
        while l.next is not None:
            result += l.val * 10 ** step
            step += 1
            l = l.next
        result += l.val * 10 ** step
        return result


solution = Solution()
x = ListNode(2, ListNode(4, ListNode(3)))
y = ListNode(5, ListNode(6, ListNode(4)))
print(solution.addTwoNumbers(x, y))
