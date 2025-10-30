class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #making valid pairs to identify them
        validPairs = {'(':')','{':'}','[':']'}
        stack = []

        for char in s:
            if char in validPairs.keys():
            #if the character is opening, add to stack
                stack.append(char)

            elif len(stack) == 0 or validPairs[stack.pop()] != char:
                #if the character is closing,
                #we need to have opening pairs in the stack
                return False
        

        return len(stack) == 0



