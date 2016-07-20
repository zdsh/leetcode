class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        ret=[]
        if len(nums1)<=0 or len(nums2)<=0:
            return ret
            
        queue=[]
        heapq.heappush(queue,[nums1[0]+nums2[0],0,0])
        
        while len(ret)<k and len(queue)>0:
            s,i,j=heapq.heappop(queue)
            ret.append([nums1[i],nums2[j]])
            if j+1<len(nums2):
                heapq.heappush(queue,[nums1[i]+nums2[j+1],i,j+1])
            if j==0 and i+1<len(nums1):
                heapq.heappush(queue,[nums1[i+1]+nums2[0],i+1,0])
        return ret

