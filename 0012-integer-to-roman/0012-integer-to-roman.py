class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        b={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}

        d=[]
        u=[]
        print(b[1000]*3)
        for i,j in enumerate(str(num)[::-1]):
            if i == 0:
                d.append(j)
            else:
                c=j
                for x in range(i):
                    c+="0"
                d.append(c)    
        print(d[::-1])
        for i in d[::-1]:
            h=0
            if len(i)==4:
                h=int(i)/1000
                u.append(b[1000]*int(h))
            elif len(i)==3:
                if int(i)>500 and int(i)<900:
                    h=(int(i)-500)/100
                    u.append(b[500]+b[100]*int(h))
                elif int(i)<400:
                    h=int(i)/100
                    u.append(b[100]*h) 
                elif int(i)==900:
                    u.append("CM")
                elif int(i)==500:
                    u.append(b[500])
                elif int(i)==400:
                    u.append("CD")
            elif len(i)==2:
                if int(i)>50 and int(i)<90:
                    h=(int(i)-50)/10
                    u.append(b[50]+b[10]*int(h))
                elif int(i)<40:
                    h=int(i)/10
                    u.append(b[10]*h) 
                elif int(i)==90:
                    u.append("XC")
                elif int(i)==50:
                    u.append(b[50])
                elif int(i)==40:
                    u.append("XL")
            elif len(i)==1:
                if int(i)>5 and int(i)<9:
                    h=(int(i)-5)/1
                    u.append(b[5]+b[1]*int(h))
                elif int(i)<4:
                    h=int(i)/1
                    u.append(b[1]*h) 
                elif int(i)==9:
                    u.append("IX")
                elif int(i)==5:
                    u.append(b[5])
                elif int(i)==4:
                    u.append("IV")
        return "".join(u) 