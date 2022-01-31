#2151 Maximum Good People Based on Statements
class Solution(object):
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        n = len(statements)
        cur_state = [-1] * n

        def dfs(state, i):
            cnt = 0
            for k in range(0, i+1):
                if state[k] == 0:
                     continue
                for t in range(i+1):
                    if statements[k][t] != 2 and statements[k][t] != state[t]:
                        return -1
                cnt += 1
            if i == n-1:
                return cnt
            state[i+1] = 0
            ret = dfs(state, i+1)
            state[i+1] = 1
            ret = max(ret, dfs(state, i+1))
            return ret

        cur_state[0] = 0
        ret = dfs(cur_state, 0)
        cur_state[0] = 1
        ret = max(ret, dfs(cur_state, 0))
        return max(0, ret)
