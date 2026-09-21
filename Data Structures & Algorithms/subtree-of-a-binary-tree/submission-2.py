# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None and subRoot is None:
            return True
        
        if root is None and subRoot is not None:
            return False
        
        if root is not None and subRoot is None:
            return True

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

            if p is None and q is None:
                return True
            
            if p is None and q is not None:
                return False
            
            if q is None and p is not None:
                return False
        
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if isSameTree(root,subRoot):
            return True
        
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        