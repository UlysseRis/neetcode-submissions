# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        diameter = 0

        def height(root: Optional[TreeNode]) -> int:

            nonlocal diameter

            if root is None:
                return 0

            leftHeight = height(root.left)
            rightHeight = height(root.right)
            
            diameter = max(diameter, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)
        
        h = height(root)

        return diameter

