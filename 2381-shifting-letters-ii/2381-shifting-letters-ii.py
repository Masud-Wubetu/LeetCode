class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        # Step 1: Build difference array
        for l, r, d in shifts:
            val = 1 if d == 1 else -1
            diff[l] += val
            if r + 1 < n:
                diff[r + 1] -= val

        # Step 2: Prefix sum to get actual shifts
        for i in range(1, n):
            diff[i] += diff[i - 1]

        # Step 3: Apply shifts
        result = []
        for i in range(n):
            shift = diff[i] % 26
            new_char = (ord(s[i]) - ord('a') + shift) % 26
            result.append(chr(new_char + ord('a')))

        return ''.join(result)