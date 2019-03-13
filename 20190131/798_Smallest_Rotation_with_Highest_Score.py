"""
File: 798_Smallest_Rotation_with_Highest_Score.py
Date: 2019/03/12 19:33:54
"""
import collections
class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
#        n = len(A)
#        lost = [0] * n
#        for i in xrange(n):
#            lost[(i - A[i] + n + 1) % n] -= 1
#        for i in xrange(1, n):
#            lost[i] += lost[i-1] + 1
#        return lost.index(max(lost))

        n, score, lost = len(A), 0, [0] * len(A)
        for i, a in enumerate(A):
            score += 1 if a <= i else 0
        for i in range(0, n):
            lost[(i - A[i] + n + 1) % n] -= 1
        lost[0] = score
        for k in range(1, n):
            lost[k] = lost[k-1] + lost[k] + 1 
        return lost.index(max(lost))

if __name__ == '__main__':
    solution = Solution()
    A = [2, 4, 1, 3, 0]
#A = [1, 3, 0, 2, 4]
#A = [2,3,1,4,0]
    print solution.bestRotation(A)
