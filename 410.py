class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        s, e = max(nums), sum(nums)
        while s < e:
            mid = (s + e) / 2
            s_num, c_num = 0, 0
            for num in nums:
                if s_num + num > mid:
                    c_num += 1
                    s_num = 0
                    if c_num > m:
                        break
                s_num += num
            if s_num > 0:
                c_num += 1
            if c_num > m:
                s = mid + 1
            else:
                e = mid
        return (s + e) / 2
            
