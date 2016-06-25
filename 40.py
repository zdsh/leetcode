class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ret=[]
        def solve(nums,cur,target):
            if target==0:
                r=cur[::]
                ret.append(r)
                return
            if len(nums)<=0:
                return
            for i in range(0,len(nums)):
                if nums[i]<=target:
                    if i>0 and nums[i]==nums[i-1]:
                        continue
                    cur.append(nums[i])
                    solve(nums[i+1:],cur,target-nums[i])
                    del cur[-1]
                else:
                    break
        solve(candidates,[],target)
        return ret
                
