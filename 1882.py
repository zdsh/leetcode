class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        from Queue import PriorityQueue
        q = PriorityQueue()
        for i in range(len(servers)):
            q.put((servers[i], i))
        ans = []
        working = PriorityQueue()

        for i in range(len(tasks)):
            if not working.empty():
                wServer = working.get()
                while wServer[0] <= i:
                    q.put((wServer[1], wServer[2]))
                    if working.empty():
                        break
                    wServer = working.get()
                if wServer[0] > i:
                    working.put(wServer)
                
            task = tasks[i]
            if q.empty():
                wServer = working.get()
                startTime = wServer[0]
                server = (wServer[1], wServer[2])
            else:
                startTime = i
                server = q.get()
            working.put((task + startTime, server[0], server[1]))
            
            ans.append(server[1])
        return ans
