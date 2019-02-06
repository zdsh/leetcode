class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 0:
            return 0
        res_odd = [1] * len(A)
        res_even = [1] * len(A)
        for i in range(1, len(A)):
            if (i - 1) % 2 == 1:
                res_odd[i] = res_odd[i - 1] + 1 if A[i - 1] > A[i] else 1
                res_even[i] = res_even[i - 1] + 1 if A[i - 1] < A[i] else 1
            else:
                res_odd[i] = res_odd[i - 1] + 1 if A[i - 1] < A[i] else 1
                res_even[i] = res_even[i - 1] + 1 if A[i - 1] > A[i] else 1
        return max(res_odd + res_even)
