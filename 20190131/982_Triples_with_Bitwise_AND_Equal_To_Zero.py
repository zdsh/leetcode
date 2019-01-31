
class Solution(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        ret = 0
        for i in range(0, len(A)):
            for j in range(0, len(A)):
                for k in range(0, len(A)):
                    if A[i] & A[j] & A[k] == 0:
                        ret += 1
        return ret

