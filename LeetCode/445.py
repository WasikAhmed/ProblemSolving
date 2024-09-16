# Add Two Numbers II

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_num(self, head: ListNode) -> int:
        num = ''
        curr = head

        while curr is not None:
            num += str(curr.val)
            curr = curr.next
        return int(num)

    def make_list(self, num: int) -> ListNode:
        num = str(num)
        head = ListNode(val=int(num[0]))
        curr = head
        for digit in num[1:]:
            new_node = ListNode(val=int(digit))
            curr.next = new_node
            curr = new_node

        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = self.get_num(l1), self.get_num(l2)
        sum = num1 + num2

        return self.make_list(sum)
