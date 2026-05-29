class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        a=0
        b=[0,]
        for i in gain:
            a+=i
            b.append(a)
        return max(b)
