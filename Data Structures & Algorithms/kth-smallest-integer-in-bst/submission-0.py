# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if root is None:
            return None
        
        result = []

        def in_order(root):

            nonlocal result

            if root is None:
                return None

            in_order(root.left)

            result.append(root.val)

            in_order(root.right)

        in_order(root)

        return result[k-1]