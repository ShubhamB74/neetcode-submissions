# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftH = self.maxH(root.left)
        rightH = self.maxH(root.right)
        d = leftH + rightH

        s = max(self.diameterOfBinaryTree(root.left), 
                self.diameterOfBinaryTree(root.right))

        return max(d, s)

    def maxH(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxH(root.left), self.maxH(root.right))

