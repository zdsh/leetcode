
class Solution(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        ret = 0
        two_dic = {}
        for i in range(0, len(A)):
            for j in range(0, len(A)):
                if A[i] & A[j] not in two_dic:
                    two_dic[A[i] & A[j]] = 0
                two_dic[A[i] & A[j]] += 1
                    
        for v in two_dic:
            for k in range(0, len(A)):
                    if v & A[k] == 0:
                        ret += two_dic[v]
        return ret

