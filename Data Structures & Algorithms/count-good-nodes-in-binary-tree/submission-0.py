# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if root is None:
            return 0
        
        result = 0

        def depth(root, max_val):
            nonlocal result

            if root is None:
                return None
            
            val = root.val
            left = root.left
            right = root.right

            if val >= max_val:
                result +=1
                depth(left, val)
                depth(right, val)
            
            else:
                depth(left, max_val)
                depth(right, max_val)
        
        depth(root, root.val)
        return result
        