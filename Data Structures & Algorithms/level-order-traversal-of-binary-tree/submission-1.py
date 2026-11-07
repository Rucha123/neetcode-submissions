# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        cur=root
        q=deque()
        q.append(cur)
        res=[]
        while q:
            ans=[]
            for i in range(len(q)):
                c1=q.popleft()
                ans.append(c1.val)
                if c1.left:
                    q.append(c1.left)
                if c1.right:
                    q.append(c1.right)
            res.append(ans)
        return res
            
            
        