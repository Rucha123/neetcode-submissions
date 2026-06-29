# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s=head
        f=head.next

        while f and f.next:
            s=s.next
            f=f.next.next

        se=s.next
        p=s.next=None

        while se:
            t=se.next
            se.next=p
            p=se
            se=t

        f=head
        se=p

        while se:
            t1=f.next
            t2=se.next
            f.next=se
            se.next=t1
            f=t1
            se=t2

        