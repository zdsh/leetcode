class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
 
        n = len(mat)
        if len(mat) == len(target):
            rot90, rot180, rot270 = True, True, True
            for i in range(0, n):
                for j in range(0, n):
                    if mat[i][j] != target[j][n - 1 - i]:
                        rot90 = False
                        break
            if rot90:
                return True
            for i in range(0, n):
                for j in range(0, n):
                    if mat[i][j] != target[n - 1 - j][i]:
                        rot270 = False
                        break
            if rot270:
                return True

            for i in range(0, n):
                for j in range(0, n):
                    if mat[i][j] != target[n - 1 - i][n - 1 - j]:
                        rot180 = False
                        break
            if rot180:
                return True
            return mat == target
        return False
