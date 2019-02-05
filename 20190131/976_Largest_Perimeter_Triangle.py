class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A_sort = sorted(A, reverse=True)
        for i in range(0, len(A_sort)-2):
            if A_sort[i+1] + A_sort[i+2] > A_sort[i]:
                return A_sort[i] + A_sort[i+1] + A_sort[i+2]
        return 0

solution = Solution()
print solution.largestPerimeter([2,1,2])
print solution.largestPerimeter([1,2,1])
print solution.largestPerimeter([3,2,3,4])
print solution.largestPerimeter([3,6,2,3])
        
