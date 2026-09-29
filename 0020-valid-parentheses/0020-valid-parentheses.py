class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a ={")": "(", "]": "[", "}": "{"}
        b=[]
        for i in s:
            print(i)
            if i in a:
                x = b.pop() if b else '#'
                print(x)
                if a[i] != x:
                    return False
            else:
                b.append(i)
        print(b)
        return not b  


        