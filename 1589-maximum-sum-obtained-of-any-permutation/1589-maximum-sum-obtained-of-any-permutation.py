class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * (n + 1)

        # Step 1: Build frequency array
        for l, r in requests:
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1

        # Prefix sum to get actual frequencies
        for i in range(1, n):
            freq[i] += freq[i - 1]

        freq = freq[:n]  # remove extra space

        # Step 2: Sort both arrays
        nums.sort()
        freq.sort()

        MOD = 10**9 + 7
        res = 0

        # Step 3: Multiply largest with largest
        for i in range(n):
            res = (res + nums[i] * freq[i]) % MOD

        return res