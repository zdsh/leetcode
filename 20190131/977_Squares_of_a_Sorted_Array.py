class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ret = []
        index = 0
        while index < len(A) and A[index] < 0:
           index += 1
        i, j = 0, index
        while i < index or j < len(A):
           if abs(A[i]) <= A[j]:
               ret.append(abs(A[i]))
               i += 1
           else:
               ret.append(A[j])
               j += 1
        while i < index:
            ret.append(abs(A[i]))
            i += 1
        while j < len(A):
            ret.append(A[j])
            j +=1
        return ret
        
