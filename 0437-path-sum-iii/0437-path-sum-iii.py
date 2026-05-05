# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        return (self.traverse(root, targetSum) +
                (self.pathSum(root.left, targetSum)) +
                (self.pathSum(root.right, targetSum)))
       
    
    def traverse(self, node, remaining):
        if not node:
            return 0
        
        count = 1 if node.val == remaining else 0

        count += self.traverse(node.left, remaining - node.val)
        count += self.traverse(node.right, remaining - node.val)

        return count