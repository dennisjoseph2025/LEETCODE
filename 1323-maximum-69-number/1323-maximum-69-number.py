class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        a = list(str(num))
        for i in a:
            print(i)
            print(type(i))
            if i =="6":
                a[a.index(i)]="9"
                break

        return int("".join(a))           

        