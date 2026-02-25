from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        if len(changed) % 2 != 0:
            return []

        original = []
        changed.sort()
        count = Counter(changed)

        for num in count:
            if count[num] == 0:
                continue

            if count[num * 2] == 0:
                return []
            
            original.append(num)
            count[num] -= 1
            count[num * 2] -= 1

        return original
        