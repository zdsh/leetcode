# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        ret = []
        if len(A) <= 0 or len(B) <= 0:
            return ret

        i, j = 0, 0
        while i < len(A) and j <= len(B):
           if A[i][1] < A[j][0]:
               i += 1
           elif A[i][0] >= A[j][1]:
               j += 1
           else:
               if A[i][0] <= A[j][0]:
                   start = A[j][0]
               else:
                   start = A[i][0]

               if A[j][1] <= A[i][1]:
                   end = A[j][1]
                   j += 1
               else:
                   end = A[i][1]
                   i += 1
               ret.append([start, end])

        return ret
