class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a=""
        for i in digits:
            a+=str(i)
        b = str(int(a)+1)

        return [int(x) for x in b]  