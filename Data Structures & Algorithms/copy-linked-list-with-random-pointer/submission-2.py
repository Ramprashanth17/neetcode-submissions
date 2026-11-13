"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #### Step-1 Create exact replica of the original LL
        if not head:
            return None
        curr = head
        while curr is not None:
            new_node = Node(curr.val)  ## instantiate a new object, but with same value as the old one
            new_node.next = curr.next ## set the connection from the new to old list next value
            curr.next = new_node ## sever the connection to old, and connect it to the new one
            curr = new_node.next ## Iterate to the next old one
        
        ### Step-2: Setting the random connections by copying the random ptrs from orginal
        curr = head
        while curr is not None:
            if curr.random is not None:
                curr.next.random = curr.random.next ## Get the new Node's random value based on og random conn.
            curr = curr.next.next ## move 2 pointers, to get to the next original list value
        
        #### Step-3: Separate the new LL from the old LL
        curr = head
        new_head = curr.next
        while curr is not None and curr.next is not None:
            copy_node = curr.next
            curr.next = copy_node.next
            
            if copy_node.next is not None:
                copy_node.next = copy_node.next.next
            
            curr = curr.next
        return new_head

