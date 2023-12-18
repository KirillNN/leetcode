# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.int_to_list(self.list_to_int(l1) + self.list_to_int(l2))

    def int_to_list(self, number: int) -> Optional[ListNode]:
        # Создаем голову списка, которая пока пуста
        head = ListNode()
        current = head

        # Преобразование числа в список
        while number:
            current.next = ListNode(number % 10)
            current = current.next
            number //= 10

        # Возвращаем список, начиная с элемента после головы
        return head.next if head.next is not None else ListNode(0)

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
# x = solution.int_to_list(123)
# pass
# x = ListNode(2, ListNode(4, ListNode(3)))
# y = ListNode(5, ListNode(6, ListNode(4)))
x = ListNode(0)
y = ListNode(0)
z = solution.addTwoNumbers(x, y)
print(z)
