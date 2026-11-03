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

        if head is None:
            return None

        cur=head
        while cur:
            copy=Node(cur.val)
            copy.next=cur.next
            cur.next=copy
            cur=copy.next

        cur=head

        while cur:
            if cur.random:
                cur.next.random=cur.random.next
            cur=cur.next.next

        
        dummy=Node(0)
        t=dummy
        cur=head

        while cur:
            copy=cur.next
            cur.next=copy.next
            t.next=copy
            t=copy
            cur=cur.next

        return dummy.next
        