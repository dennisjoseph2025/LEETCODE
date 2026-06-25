class Solution(object):
    def isPowerOfFour(self, n):
        a = {pow(4, i) for i in range(16)}       
        return n in a