# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return true

        prev=None

        st=[]
        cur=root

        while cur or st:
            while cur:
                st.append(cur)
                cur=cur.left

            cur=st.pop()

            if prev is not None and prev.val>=cur.val:
                return False
            prev =cur

            cur=cur.right
        return True
        