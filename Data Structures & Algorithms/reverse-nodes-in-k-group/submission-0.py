# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy ### pointer before the group start
    
        while True:
            kth = self.getKth(group_prev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prev = kth.next
            curr = group_prev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # Save the old start of the group (which is now the tail)
            tail_of_current_group = group_prev.next
            
            # Connect previous group to the new head (kth)
            group_prev.next = kth
            
            # Connect the tail of the current group to the next group's start
            tail_of_current_group.next = groupNext
            
            # Move group_prev forward to be the tail of the current group
            group_prev = tail_of_current_group
        
        return dummy.next
    
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
