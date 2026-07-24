class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        a=[]
        n=0
        if ruleKey == "type":
            n=0
        if ruleKey == "color":
            n=1
        if ruleKey == "name":
            n=2
        for i in items:
            if i[n]==ruleValue:
                a.append(i)
        return len(a)        

        