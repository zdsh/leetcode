class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0:
            return 2147483647
        sig=True
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            sig=False
        dividend,divisor=abs(dividend),abs(divisor)
        i,ret=0,0
        print(dividend,divisor)
        while dividend>=divisor:
            while dividend>=divisor<<i:
                dividend-=divisor<<i
                ret+=1<<i
                i+=1
            i=0
        if not sig:
            ret=-ret
        return min(ret,2147483647)

