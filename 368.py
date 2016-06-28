class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        nums.sort()
        res=defaultdict(lambda:1)
        depth_dic=defaultdict(lambda:[])
        for num in nums:
            v=1
            depth_list=depth_dic.keys()
            depth_list.sort(reverse=True)
            for depth in depth_list:
                for p in depth_dic[depth]:
                    if num%p==0:
                        v=depth+1
                        break
                if v>1:
                    break
            depth_dic[v].append(num)
        depth_list=depth_dic.keys()
        depth_list.sort(reverse=True)
        ret=[]
        for d in depth_list:
            if len(ret)<=0:
                ret.append(depth_dic[d][0])
            else:
                for p in depth_dic[d]:
                    if ret[-1]%p==0:
                        ret.append(p)
                        break
                    
        return ret[::-1]
