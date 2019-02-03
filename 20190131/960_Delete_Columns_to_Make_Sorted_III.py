"""
File: 960_Delete_Columns_to_Make_Sorted_III.py
Date: 2019/02/03 13:01:29
"""
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if len(A) <= 0 or len(A[0]) <=0 :
            return 0
        result = [1] * len(A[0])
        for i in range(1, len(A[0])):
            value = result[i]
            for j in range(0, i):
                k = 0
                while k < len(A) and A[k][j] <= A[k][i]:
                    k+=1
                if k == len(A):
                    value = max(value, result[j] + 1)
            result[i] = value
        return len(A[0]) - max(result)

if __name__ == '__main__':
    solution = Solution()
    A = ["abbba"]
    print solution.minDeletionSize(A)
        
