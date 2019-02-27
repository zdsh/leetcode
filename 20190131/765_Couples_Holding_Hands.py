"""
File: 765_Couples_Holding_Hands.py
Date: 2019/02/27 15:14:43
"""
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n, res = len(row), 0
        row_dic = {}
        for k, s in enumerate(row):
            row_dic[s] = k
        def findCouple(k):
            return k + 1 if k % 2 == 0 else k - 1

        for i in range(0, n, 2):
            couple = findCouple(row[i])
            if couple == row[i+1]:
                continue
            row[row_dic[couple]] = row[i+1]
            row_dic[row[i+1]], row_dic[couple] = row_dic[couple], i + 1
            row[i+1] = couple
            res += 1
        return res 

if __name__ =='__main__':
    solution = Solution()
    row = [1,4,0,5,8,7,6,3,2,9]
    print solution.minSwapsCouples(row)
