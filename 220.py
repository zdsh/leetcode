class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        data={}
        for index,num in enumerate(nums):
            data[index]=num
        data=sorted(data.iteritems(),key=lambda x:x[1])
        print data
        for i in range(0,len(data)-1):
            j=i+1
            while j<len(data) and abs(data[j][1]-data[i][1])<=t:
                if abs(data[j][0]-data[i][0])<=k:
                    return True
                j+=1
        return False
