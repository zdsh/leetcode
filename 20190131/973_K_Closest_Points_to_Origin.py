class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distance_list = []
        for i in range(0, len(points)):
            distance_list.append(points[i][0]*points[i][0] + points[i][1]*points[i][1])
        distance_list.sort()
        ret = []
        for i in range(0, len(points)):
            if points[i][0]*points[i][0] + points[i][1]*points[i][1] <= distance_list[K-1]:
                ret.append(points[i])
        return ret
        
