# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
        
        res = True
        def height(root: Optional[TreeNode]):

            nonlocal res

            if root is None:
                return 0
            
            leftHeight = height(root.left)
            rightHeight = height(root.right)

            res = res and (abs(leftHeight - rightHeight) <= 1)

            return 1 + max(leftHeight,rightHeight)

        height(root)
        
        return res 