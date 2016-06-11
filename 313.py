class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        def multiple(x,y):
            return x*y
        if n==1:
            return 1
        ret=[1]
        i=1
        index=[0]*len(primes)
        while i<=n-1:
            new_value_list=map(multiple,[ret[k] for k in index], primes)
            new_value=min(new_value_list)
            ret.append(new_value)
            for k,value in enumerate(new_value_list):
                if value==new_value:
                    index[k]+=1
            i+=1
        return ret[n-1]
            
