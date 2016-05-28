class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
	for num in nums1:
	    if num in nums2:
                res.append(num)
                nums2=filter(lambda a:a!=num,nums2)
        return res

s=Solution()
print(s.intersect([1,2,2,1],[2,2]))
