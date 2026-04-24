class Solution:
    def countKeyChanges(self, s):
        s = s.lower()  
        ch = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ch += 1
        return ch
        