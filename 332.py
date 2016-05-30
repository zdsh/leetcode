class Solution(object):
    def dfs(self,cur,n,itineraries):
        if len(self.ret)==n:
            return True
        if cur in itineraries:
            for city,c in itineraries[cur].items():
                if c!=0:
                    itineraries[cur][city],self.ret=itineraries[cur][city]-1,self.ret+[city]
                    if self.dfs(city,n,itineraries):
                        return True
                    itineraries[cur][city],self.ret=itineraries[cur][city]+1,self.ret[:-1]
        return False
        
        
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        n,self.ret=len(tickets)+1,['JFK']
        itineraries=collections.defaultdict(lambda:collections.OrderedDict())
        for b,e in sorted(tickets):
            itineraries[b].setdefault(e,0)
            itineraries[b][e]+=1
        self.dfs('JFK',n,itineraries)
        return self.ret
