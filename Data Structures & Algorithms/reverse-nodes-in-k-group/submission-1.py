# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
    def reverse_group(self, start, anchor):
        prev, curr = anchor, start
        while curr != anchor:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.getKth(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next
            group_start = group_prev.next

            ### Reverse the group
            self.reverse_group(group_start, group_next)

            ### Stitch the group back into list
            group_prev.next = kth
            group_prev = group_start
        
        return dummy.next

