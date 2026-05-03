class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, current: List, remainder: int):
            if remainder == 0:
                res.append(list(current))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remainder:
                    break
                
                current.append(candidates[i])
                backtrack(i, current, remainder - candidates[i])
                current.pop()
        
        candidates.sort()
        backtrack(0, [], target)
        return res