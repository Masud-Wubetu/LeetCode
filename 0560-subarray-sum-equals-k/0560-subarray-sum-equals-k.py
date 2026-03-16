from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        
        prefix_sum = 0
        result = 0
        
        for num in nums:
            prefix_sum += num
            
            if prefix_sum - k in count:
                result += count[prefix_sum - k]
            
            count[prefix_sum] += 1
        
        return result