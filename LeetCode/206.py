# Reverse Linked List

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def print_list(self, node: ListNode):
        while node is not None:
            print(f'{node.val}', end="->")
            node = node.next
        print('None')


if __name__ == '__main__':
    head = ListNode(val=10)
    node2 = ListNode(val=20)
    node3 = ListNode(val=30)
    node4 = ListNode(val=40)
    node5 = ListNode(val=50)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()

    s.print_list(head)
    reversed_list = s.reverseList(head)
    s.print_list(reversed_list)
