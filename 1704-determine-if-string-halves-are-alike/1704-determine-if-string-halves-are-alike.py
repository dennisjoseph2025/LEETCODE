class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b=s[:int(len(s)/2)]
        c=s[int(len(s)/2):]
        e = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v1 = 0
        v2 = 0
        for i in b:
            if i in e:
                v1+=1
        for i in c:
            if i in e:
                v2+=1
        if v1 == v2:
            return True
        else:
            return False