class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        ret = []
        if x == 1 amd y == 1:
            return [2]
        x_power  = 1
        while x_power < bound:
            y_power = 1
            while x_power + y_power <= bound:
                ret.append(x_power + y_power)
                y_power *= y
                if y_power == y:
                    break
            x_power *= x
            if x_power == x:
                break
        return list(set(ret))
