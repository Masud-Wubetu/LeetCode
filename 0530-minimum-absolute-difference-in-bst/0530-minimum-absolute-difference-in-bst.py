# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        prev = None
        ans = float("inf")

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if prev is not None:
                ans = min(ans, root.val - prev)

            prev = root.val

            root = root.right

        return ans