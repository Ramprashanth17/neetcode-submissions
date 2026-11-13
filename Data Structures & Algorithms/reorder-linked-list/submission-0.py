# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        ## Cutting the 2nd half
        second_half = slow.next
        slow.next = None
        # Reversing the second half
        prev = None
        curr = second_half
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        ## Merging the two halves
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            # Interleave the nodes
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2