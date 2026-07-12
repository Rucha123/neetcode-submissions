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

        q=deque()
        q.append(root)
        res=[]

        while q:
            ans=[]
            for i in range(len(q)):
                cur=q.popleft()
                ans.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(ans)

        return res

        