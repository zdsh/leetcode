class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        visited = {start:1}
        def bfs(start, end, bank, d):
            if start == end:
                return d
            
            ret = -1
            for i in range(0, len(start)):
                for mu in ['A', 'C', 'G', 'T']:
                    start_ = start[0:i] + mu + start[i+1:]
                    if start_ not in bank or start_ in visited:
                        continue
                    visited[start_] = 1
                    ret_ = bfs(start_, end, bank, d+1)
                    if ret_ != -1 and ret != -1:
                        ret = min(ret, ret_)
                    elif ret_ != -1:
                        ret = ret_
            print(start, end, d, ret)
            return ret
        return bfs(start, end, bank, 0)        
