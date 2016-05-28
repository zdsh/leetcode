class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        b_num=bin(num)
        b_num=b_num[2:]
        while len(b_num)>2:
            if b_num[len(b_num)-2:]=='00':
                b_num=b_num[:len(b_num)-2]
            else:
                return False
        if len(b_num)==1 and b_num=='1':
            return True
        else:
            return False
