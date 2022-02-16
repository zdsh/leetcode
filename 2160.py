class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = [n for n in list(str(num)) if n!='0']
        a.sort()
        n1 = ''.join([n for i,n in enumerate(a) if i % 2 == 0])
        n2 = ''.join([n for i,n in enumerate(a) if i % 2 == 1])
        if n2 == '':
            n2 = 0
        return int(n1) + int(n2)
