class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def vowel_count(x):
            e = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            v = 0
            for i in x:
                if i in e:
                    v+=1
            return v
        return vowel_count(s[:int(len(s)/2)]) == vowel_count(s[int(len(s)/2):])          