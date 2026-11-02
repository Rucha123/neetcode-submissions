# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mh=[]
        head=cur=ListNode(None)

        for i in lists:
            while i:
                heapq.heappush(mh,i.val)
                i=i.next

        while mh:
            cur.next=ListNode(heapq.heappop(mh))
            cur=cur.next

        return head.next
        