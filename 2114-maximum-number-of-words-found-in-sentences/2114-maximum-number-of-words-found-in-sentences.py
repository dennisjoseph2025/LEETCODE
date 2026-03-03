class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        a =0
        b= 0
        for i in sentences:
            a = len(i.split())
            if a>b:
                b = a

        return b