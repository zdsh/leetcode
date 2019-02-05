class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        ret = []
        x_power  = 1
        while x_power < bound:
            y_power = 1
            while x_power + y_power <= bound:
                ret.append(x_power + y_power)
                y_power *= y
            x_power *= x
        return ret
