# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        st=[]
        c=0
        cur=root
        m=float("-inf")

        while cur or st:
            while cur:
                if cur.val>=m:
                    m=cur.val
                st.append([cur,m])
                cur=cur.left
            cur,m=st.pop()
            if cur.val >= m:
                c+=1
            cur=cur.right

        return c
             

    
        