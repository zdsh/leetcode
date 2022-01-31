class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        data = {}
        for item in arr:
            if item * 2 in data:
                return True
            if item % 2 == 0 and item / 2 in data:
                return True
            data[item] = 1
        return False
