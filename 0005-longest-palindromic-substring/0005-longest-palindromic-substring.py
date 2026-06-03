class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        maxStr = 0

        for i in range(len(s)):
            
            l = i
            r = i

            while (l >= 0 and r < len(s) and s[l] == s[r]):
                if (r - l + 1 > maxStr):
                    maxStr = r - l + 1
                    start = l
                
                l -= 1
                r += 1
            
            l = i
            r = i + 1

            while (l >= 0 and r < len(s) and s[l] == s[r]):
                if (r - l + 1 > maxStr):
                    maxStr = r - l + 1
                    start = l
                
                l -= 1
                r += 1
            
        return s[start:start + maxStr]



        