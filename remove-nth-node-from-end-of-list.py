# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_nodes = []
        while head.next is not None:
            list_nodes.append(head.val)
            head = head.next
        list_nodes.append(head.val)
        list_nodes.pop(len(list_nodes) - n)
        head = ListNode(0)
        current = head
        for i in list_nodes:
            current.next = ListNode(i)
            current = current.next

        return head.next if len(list_nodes) > 0 else None


solution = Solution()
# x = solution.int_to_list(123)
# pass
# x = ListNode(2, ListNode(4, ListNode(3)))
# y = ListNode(5, ListNode(6, ListNode(4)))
# x = ListNode(0)
# y = ListNode(0)
x = ListNode(2, ListNode(4, ListNode(3)))
z = solution.removeNthFromEnd(x, 1)
print(z)
