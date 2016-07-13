#The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low,high=1,n
        ret=guess((low+high)/2)
        while ret!=0:
            if ret==-1:
                high=(low+high)/2-1
            if ret==1:
                low=(low+high)/2+1
            ret=guess((low+high)/2)
        return (low+high)/2
