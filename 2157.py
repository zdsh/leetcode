class Solution(object):
    def groupStrings(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        values = {sum(1<<(ord(w)-ord('a')) for w in word):id for id,word in enumerate(words)}
        G = {id:set() for id, word in enumerate(words)}

        for id, word in enumerate(words):
            pos = [ord(w)-ord('a') for w in word]
            value = sum(1<<p for p in pos)
            if value in values and values[value] != id:
                G[id].add(values[value])
                G[values[value]].add(id)
            for p in pos:
                c_value = value - (1<<p)
                if c_value in values:
                    G[id].add(values[c_value])
                    G[values[c_value]].add(id)
                values[c_value] = id                
           
        visited, com, m_c = set(), 0, 0
        for id, word in enumerate(words):
            if id in visited:
                continue
            q, c = [id], 1
            visited.add(id)
            while q:
                w = q.pop()
                for e in G[w]:
                    if e not in visited:
                         q.append(e)
                         visited.add(e)
                         c+=1
                         
            com += 1
            m_c = max(c, m_c)
        return [com, m_c]
