class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        countMap = {}

        for i, num in enumerate(nums):
            d = target - num

            if d in countMap:
                return [countMap[d], i]
            
            countMap[num] = i
        
    

            