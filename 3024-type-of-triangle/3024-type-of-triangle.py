class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort()
        if nums[0]+nums[1]<= nums[2]:
            return 'none'
        a,b,c=nums
        if a==b and b==c:
            return 'equilateral'
        elif a==b or b==c or a==c:
            return 'isosceles'
        else:
            return 'scalene'        