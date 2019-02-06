class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        even_sum = 0
        for v in A:
            if v % 2 == 0:
                v += v
        ret = []
        for query in queries:
            if A[query[1]] % 2 == 0:
                even_sum -= A[query[1]]
            A[query[1]] += query[0]
            if A[query[1]] % 2 == 0:
                even_sum += A[query[1]]
            ret.append(even_sum)
        return ret
