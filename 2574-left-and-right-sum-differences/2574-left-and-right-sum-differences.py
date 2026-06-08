class Solution(object):
    def leftRightDifference(self, nums):
        answer = []
        left_sum = 0
        right_sum = sum(nums) 
        
        for num in nums:
            right_sum -= num
            answer.append(abs(left_sum - right_sum))
            left_sum += num      
        return answer
