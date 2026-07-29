class Solution(object):
    def maxFreqSum(self, s):
        a=0
        b=0
        for i in s:
            if i in "aeiou":
                if a<=s.count(i):
                    a=s.count(i)
            else:
                if b<=s.count(i):
                    b=s.count(i)
        return a+b