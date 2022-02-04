class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        s, e = max(weights), sum(weights)
        while s < e:
            mid = (s + e) / 2
            cur_day_sum, c_day = 0, 0
            for w in weights:
                if cur_day_sum + w > mid:
                    c_day += 1
                    cur_day_sum = 0
                    if c_day > days:
                        break
                cur_day_sum += w
            if cur_day_sum > 0:
                c_day += 1
            if c_day <= days:
                e = mid
            else:
                s = mid + 1
        return (s + e) / 2        
