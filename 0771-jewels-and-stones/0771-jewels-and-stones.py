class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        a=0
        for i in stones:
            a+=jewels.count(i)
        return a      