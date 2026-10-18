# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p==root or q==root or root is None:
            return root

        left=self.lowestCommonAncestor(root.left,p,q)
        rt=self.lowestCommonAncestor(root.right,p,q)

        if left and rt:
            return root
        return left if left else rt

        