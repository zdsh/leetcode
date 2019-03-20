"""
File: 728_Self_Dividing_Numbers.py
Date: 2019/03/20 15:29:16
"""
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [num for num in range(left, right+1) if num%10 != 0 and all(f!='0' and num%int(f)==0 for f in str(num))]
