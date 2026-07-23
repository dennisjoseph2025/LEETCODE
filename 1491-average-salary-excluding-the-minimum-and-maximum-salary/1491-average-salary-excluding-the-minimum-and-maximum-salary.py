class Solution(object):
    def average(self, salary):
        a=sorted(salary)[1:-1]
        return float(sum(a))/len(a)