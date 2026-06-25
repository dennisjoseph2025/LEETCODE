class Solution(object):
    def isPowerOfTwo(self, n):
        a = {pow(2, i) for i in range(36)}
        return n in a