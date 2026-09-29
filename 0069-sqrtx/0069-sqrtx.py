import math
class Solution(object):
    def mySqrt(self, x):
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        if x == 0:
            return 0
        guess = x / 2.0
        while abs(guess * guess - x) > 0.00001:
            guess = (guess + x / guess) / 2.0   
        
        return int(guess)