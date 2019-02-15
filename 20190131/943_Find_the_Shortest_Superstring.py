"""
File: 943_Find_the_Shortest_Superstring.py
Date: 2019/02/15 12:42:06
"""

class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        def calcOverlap(s1, s2):
            m = len(s1)
            for i in xrange(m):
                if s1[i:] == s2[0:m - i]:
                    return m - i
            return 0
        
        n = len(A)
        overlap_dic = {}
        for i in range(0, n):
            for j in range(0, n):
                if i != j:
                    overlap_dic[i, j] = calcOverlap(A[i], A[j])
        overlap_sort = sorted(overlap_dic.items(), key=lambda v:v[1], reverse = True)
 
        overlaped = [0] * n
        connect_dic = {}
        i = 0
        while i < n - 1:
            (s1_id, s2_id) = overlap_sort[0][0]
            if overlaped[s1_id] != 0 or s2_id in connect_dic:
                del overlap_sort[0]
                continue
            l = s1_id
            while l in connect_dic:
                l = connect_dic[l][0]
            if l == s2_id:
                del overlap_sort[0]
                continue
                
            overlaped[s1_id] = 1
            connect_dic[s2_id] = (s1_id, overlap_sort[0][1])
            del overlap_sort[0]
            i += 1

        ret = ''
        for i in xrange(n):
            if overlaped[i] == 0:
               s2_id = i
               while s2_id in connect_dic:
                   ret = A[s2_id][connect_dic[s2_id][1]:] + ret
                   s2_id = connect_dic[s2_id][0]
               ret = A[s2_id] + ret
               break  
        return ret

if __name__ == '__main__':
    solution = Solution()
    A = ["alex","loves","leetcode"]
#A = ["catg","ctaagt","gcta","ttca","atgcatc"]
#A = ["ymv","lpkp","ajelp","kpx"]
    print solution.shortestSuperstring(A)
