"""
File: 795_Number_of_Subarrays_with_Bounded_Maximum.py
Date: 2019/03/13 14:07:34
"""
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        n = len(A)
        b, dp = -1, [0] * n
        for i in range(n):
            if A[i] <= R:
                if A[i] >= L:
                    dp[i] = dp[i-1] + 1 if i > 0 else 1
                    if b != -1:
                        dp[i] += i - b
                    b = -1
                else:
                    dp[i] = dp[i-1] if i > 0 else 0
                    if b == -1:
                        b = i
            else:
                b = -1
        return sum(dp)      

if __name__ == '__main__':
    sol = Solution()
    A = [16,69,88,85,79,87,37,33,39,34]
    L = 55
    R = 57
    A = [876,880,482,260,132,421,732,703,795,420,871,445,400,291,358,589,617,202,755,810,227,813,549,791,418,528,835,401,526,584,873,662,13,314,988,101,299,816,833,224,160,852,179,769,646,558,661,808,651,982,878,918,406,551,467,87,139,387,16,531,307,389,939,551,613,36,528,460,404,314,66,111,458,531,944,461,951,419,82,896,467,353,704,905,705,760,61,422,395,298,127,516,153,299,801,341,668,598,98,241]
    L = 658
    R = 719
    print sol.numSubarrayBoundedMax(A, L, R)
