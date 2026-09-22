# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        val_r = root.val
        val_p = p.val
        val_q = q.val

        if val_p < val_r and val_q < val_r:
            return self.lowestCommonAncestor(root.left,p,q)
        
        elif val_p > val_r and val_q > val_r:
            return self.lowestCommonAncestor(root.right,p,q)

        else:
            return root