class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        a =[]
        maxcandies = max(candies)
        for i in candies:
            a.append(i + extraCandies >= maxcandies)

        return a