class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        ret = []
        if x == 1 and y == 1:
            return [2]
        x_power  = 1
        while x_power < bound:
            y_power = 1
            while x_power + y_power <= bound:
                ret.append(x_power + y_power)
                y_power *= y
                if y == 1:
                    break
            x_power *= x
            if x == 1 :
                break
        return list(set(ret))

if __name__ == '__main__':
    solution = Solution()
    print solution.powerfulIntegers(1, 1, 10)
    print solution.powerfulIntegers(1, 2, 100)
    print solution.powerfulIntegers(2, 3, 10)
    print solution.powerfulIntegers(3, 5, 15)
