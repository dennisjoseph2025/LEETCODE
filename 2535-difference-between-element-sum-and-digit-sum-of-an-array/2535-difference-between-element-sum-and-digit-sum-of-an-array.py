class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a= 0
        c=0
        for i in nums:
            a+=i
        b= "".join(str(j)for j in nums)
        for i in b:
            c+=int(i)
        return a - c    
            