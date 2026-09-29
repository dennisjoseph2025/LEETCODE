class Solution(object):
    def isValid(self, s):
        a ={")": "(", "]": "[", "}": "{"}
        b=[]
        for i in s:
            if i in a:
                x = b.pop() if b else '#'
                if a[i] != x:
                    return False
            else:
                b.append(i)
        return not b  


        