class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def similar(id1, id2):
            c = 0
            if len(strs[id1]) != len(strs[id2]):
                return False
            for i in range(len(strs[id1])):
                if strs[id1][i] != strs[id2][i]:
                    c += 1
            if c == 0 or c == 2:
                return True
            return False

        visited, ret = set(), 0
        for id, str in enumerate(strs):
            if id in visited:
                continue
            q = [id]
            visited.add(id)
            while q:
               cur_id = q.pop()
               for k in range(len(strs)):
                   if k in visited:
                       continue
                   if similar(cur_id, k):
                       q += [k]
                       visited.add(k)
            ret += 1
        return ret        
