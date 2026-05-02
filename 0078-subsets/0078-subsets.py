class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(s, c):
            res.append(c[:])

            for i in range(s, len(nums)):
                c.append(nums[i])
                backtrack(i + 1, c)
                c.pop()
        
        backtrack(0, [])
        return res


