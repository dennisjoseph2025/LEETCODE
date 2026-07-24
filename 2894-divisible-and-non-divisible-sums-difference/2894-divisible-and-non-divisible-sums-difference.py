class Solution(object):
    def differenceOfSums(self, n, m):
        non_divisible=[]
        divisible=[]
        for i in range(1,n+1):
            if i%m!=0:
                non_divisible.append(i)
            elif i%m==0:
                divisible.append(i)
        return sum(non_divisible)-sum(divisible)            
        