# Add Two Numbers

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_reverse_num(self, head: ListNode):
        reverse_num = ''
        curr = head

        while curr is not None:
            reverse_num += str(curr.val)
            curr = curr.next

        return int(reverse_num[::-1])

    def make_list(self, num1: int, num2: int) -> ListNode:
        reversed_sum = str(num1 + num2)[::-1]
        head = ListNode(val=int(reversed_sum[0]), next=None)
        curr = head
        for digit in reversed_sum[1:]:
            new_node = ListNode(val=int(digit), next=None)
            curr.next = new_node
            curr = new_node

        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = self.get_reverse_num(l1), self.get_reverse_num(l2)
        return self.make_list(num1, num2)
