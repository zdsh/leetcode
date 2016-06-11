class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge_sort(data):
            if len(data)<=1:
                return data
            mid=len(data)/2
            left,right=merge_sort(data[0:mid]),merge_sort(data[mid:])
            m,n=len(left),len(right)
            i,j=0,0
            while i<m or j<n:
                if j==n or i<m and left[i][1]<=right[j][1]:
                    data[i+j]=left[i]
                    self.ret[left[i][0]]+=j
                    i+=1
                else:
                    data[i+j]=right[j]
                    j+=1
            return data
        
        self.ret=[0]*len(nums)
        merge_sort(list(enumerate(nums)))
        return self.ret
