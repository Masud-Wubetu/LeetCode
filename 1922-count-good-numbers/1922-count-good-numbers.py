class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        e = (n + 1) // 2
        o = n // 2

        return (pow(5, e, MOD) * pow(4, o, MOD)) % MOD
        
            
        