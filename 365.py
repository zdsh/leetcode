class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(x,y):
            if x==0 or y==0:
                return 0
            if x>y:
                return gcd(y,x)
            if y%x==0:
                return x
            return gcd(y%x,x)
            
        if x+y<z:
            return False
        if z==0:
            return True
        v=gcd(x,y)
        if v==0:
            return z==x or z==y
        else:
            return z%v==0
           
