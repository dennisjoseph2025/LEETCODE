class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = "".join(re.sub(r'[^\w\s]|_', '', s).lower().split())
        print(a)
        return a == a[::-1]
        