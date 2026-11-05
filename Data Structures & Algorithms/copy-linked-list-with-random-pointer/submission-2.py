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
            cp=Node(cur.val)
            cp.next=cur.next
            cur.next=cp
            cur=cp.next

        cur=head
        while cur:
            if cur.random:
                cur.next.random=cur.random.next
            cur=cur.next.next

        dummy=Node(0)
        t=dummy
        cur=head
        while cur:
            cp=cur.next
            cur.next=cp.next
            t.next=cp
            t=cp
            cur=cur.next

        return dummy.next



        