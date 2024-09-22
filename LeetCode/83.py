# Remove Duplicates from Sorted List

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head:
        #     return None
        #
        # hashset = set()
        # hashset.add(head.val)
        # curr = head
        #
        # while curr.next is not None:
        #     if curr.next.val in hashset:
        #         curr.next = curr.next.next
        #     else:
        #         hashset.add(curr.next.val)
        #         curr = curr.next
        # return head

        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
