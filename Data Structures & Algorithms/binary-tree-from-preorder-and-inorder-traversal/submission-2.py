# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        index_map = {value: i for i, value in enumerate(inorder)}

        index = 0
        l = 0
        r = len(inorder) - 1

        def build(l,r):
            nonlocal index

            if l > r:
                return None  

            node = TreeNode(preorder[index])
            mid = index_map[preorder[index]]
            index += 1
            node.left = build(l,mid-1)
            node.right = build(mid+1,r)

            return node
    
        return build(l,r)