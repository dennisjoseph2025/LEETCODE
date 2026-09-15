class Solution(object):
    def findDuplicates(self, nums):
        a = []
        for i in nums:
            index = abs(i) - 1
            if nums[index] < 0:
                a.append(abs(i))
            else:
                nums[index] = -nums[index]
        return a