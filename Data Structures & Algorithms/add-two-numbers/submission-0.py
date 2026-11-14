# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer_ll = ListNode(0)
        carry = 0
        ptr = answer_ll

        while l1 or l2 or carry:
            sum = 0 + carry

            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            
            carry = sum // 10
            sum = sum % 10
            ptr.next = ListNode(sum)
            ptr = ptr.next

        
        return answer_ll.next