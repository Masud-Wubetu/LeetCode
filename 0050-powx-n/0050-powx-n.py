class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #getting power of x to absolute value of n
        result = self.myPositivePow(x, abs(n))
        
        #if n is negative reverse the result
        if(n < 0):
            result = 1 / result

        return result
    
    def myPositivePow(self, x, n):
        #any number raised to 0 is 1.0
        if(n == 0):
            return 1.0
        
        #do the half computation
        halfPower = self.myPositivePow(x, n // 2)
        fullPower = halfPower * halfPower

        #if the power is odd, multiply fullPower by x
        if(n % 2 != 0):
            fullPower *= x

        return fullPower
        
