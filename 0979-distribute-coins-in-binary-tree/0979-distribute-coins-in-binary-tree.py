# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.move_count = 0

        def dfs(curr):
            if not curr:
                return 0
            
            lec = dfs(curr.left)
            rec = dfs(curr.right)

            tec = curr.val - 1 + lec + rec

            self.move_count += abs(tec)

            return tec

        dfs(root)
        return self.move_count
