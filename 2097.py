class Solution(object):
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        deg = defaultdict(int)
        edges = defaultdict(list)
        for pair in pairs:
            [u, v] = pair
            deg[u] -= 1
            deg[v] += 1
            edges[u].append(v)

        s_arr = pairs[0][0]
        for s in deg:
            if deg[s] == -1:
                s_arr = s
        stack = [s_arr]
        route = []
        while stack:
            while edges[stack[-1]]:
                stack.append(edges[stack[-1]].pop())
            route.append(stack.pop())
        route = route[::-1]
        return [[route[i], route[i+1]] for i in range(0, len(route)-1)]
