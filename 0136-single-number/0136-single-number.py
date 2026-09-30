class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        b=[]
        for i in nums:
            if i not in a:
                a.append(i)
            else:
                b.append(i)   
        for i in b:
            a.remove(i)
        return a[0]           