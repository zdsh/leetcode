"""
File: 957_Prison_Cells_After_N_Days.py
Date: 2019/02/01 15:05:31
"""
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        recode = []
        recode.append(cells)
        day = 1
        while day <= N:
            new_cells=[0]
            for j in range(1, len(cells)-1):
                if cells[j - 1] == cells[j + 1]:
                    new_cells.append(1)
                else:
                    new_cells.append(0)
            new_cells.append(0)
            for i in range(0, len(recode)):
                if recode[i] == new_cells:
                    return recode[i:][(N-day)%(day-i)]                
            recode.append(new_cells)
            cells = new_cells
            day += 1
        return recode[-1] 

if __name__ =='__main__':
    solution = Solution()
    print solution.prisonAfterNDays([0,1,0,1,1,0,0,1], 7)
    print solution.prisonAfterNDays([1, 1, 0, 1, 1, 0, 1, 1], 6)
    print solution.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000) 
    print solution.prisonAfterNDays([1, 0, 0, 1, 0, 0, 0, 1], 826)
