# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.move = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.move += abs(left) + abs(right)

            return curr.val - 1 + left + right
        
        dfs(root)

        return self.move

        