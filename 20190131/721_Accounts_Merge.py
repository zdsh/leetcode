"""
File: 721_Accounts_Merge.py
Date: 2019/03/20 10:45:48
"""
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        res = {}
        def find(x):
            while x in res and x != res[x]:
                x = res[x]
            return x

        def union(x, y):
            px = find(x)
            py = find(y)
            res[py] = px

        ret, emailNameMap = set(), {}
        for account in accounts:
            emails = account[1:]
            emailNameMap[emails[0]] = [account[0]]
            for e in emails:
                union(emails[0], e)

        for v in res:
            p = find(v)
            ret.add(p)
            emailNameMap[p] += [v]
        return [[emailNameMap[k][0]] + sorted(emailNameMap[k][1:]) for k in ret]        

if __name__ == '__main__':
    sol = Solution()
    accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
#accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    print sol.accountsMerge(accounts)
