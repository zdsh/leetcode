"""
File: 983_Minimum_Cost_For_Tickets.py
Date: 2019/01/31 15:30:47
"""
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        if len(days) <= 0:
            return 0
        mini_costs = [0] * 366
        index = len(days)
        mini_costs[days[-1]] = min(costs)

        index = index - 2
        while index >= 0:
            value = mini_costs[days[index+1]] + min(costs)
            value_day1 = mini_costs[days[index+1]] + costs[0]
            value_day2 = costs[1] 
            for k in range(index+1, len(days)):
                if days[k] - days[index] >= 7:
                    value_day2 = mini_costs[days[k]] + costs[1] 
                    break
            value_day30 = costs[2]
            for k in range(index+1, len(days)):
                if days[k] - days[index] >= 30:
                    value_day30 = mini_costs[days[k]] + costs[2] 
                    break
            mini_costs[days[index]] = min([value, value_day1, value_day2, value_day30])
            #print mini_costs[days[index]], [value, value_day1, value_day2, value_day30]
            index -= 1

        return mini_costs[days[0]]

if __name__ == '__main__':
    solution = Solution()
    #print solution.mincostTickets([1,4,6,7,8,20], [2,7,15])
    print solution.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15])
           

