class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        num1 = (num - 3) // 3
        if num % 3 != 0:
            return []
        

        return [num1, num1 + 1, num1 + 2]