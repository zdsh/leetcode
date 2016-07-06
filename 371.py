class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b==0 or a==0:
            return a or b
        if a*b<0:
            if b<0:
                return self.getSum(b,a)
            v=self.getSum(~a,1)
            if v==b:
                return 0
            if v<b:
                return self.getSum(~self.getSum(v,self.getSum(~b,1)),1)
        return self.getSum(a^b, (a&b)<<1)

