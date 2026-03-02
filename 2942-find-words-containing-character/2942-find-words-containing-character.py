class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        a= []
        for id,i in enumerate(words):
            if x in i:
                a.append(id)
        return a        
        