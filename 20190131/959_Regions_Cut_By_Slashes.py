"""
File: 959_Regions_Cut_By_Slashes.py
Date: 2019/02/02 12:18:30
"""
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        if len(grid) <= 0:
            return 0
        recode = []
        for i in range(0, len(grid)):
            row_recode =[]
            for j in range(0, len(grid[i])):
                row_recode.append([0, 0, 0, 0])
            recode.append(row_recode)

        id = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                for region_id in range(0, len(recode[row][col])):
                    if recode[row][col][region_id] != 0:
                        id += 1
                        recode[row][col][region_id] = id
                        search_list =[[row, col, region_id]]
                        index = 0
                        while len(search_list) > index:
                            [x, y, p] = search_list[index]
                            index += 1
                            if grid[x][y] == ' ':
                                 for i in range(0, 4):
                                     if recode[x][y][i] == 0:
                                         recode[x][y][i] = id
                                         search_list.append([x, y, i ])

                            if grid[x][y] == '/':     
                                if p <= 1:
                                    for i in range(0, 2):
                                        if recode[x][y][i] == 0:
                                            recode[x][y][i] = id
                                            search_list.append([x, y, i ])
                                if p >= 2:
                                    for i in range(2, 4):
                                        if recode[x][y][i] == 0:
                                            recode[x][y][i] = id
                                            search_list.append([x, y, i ])
   
                            if grid[x][y] == '\\':
                                if p >= 1 and p <= 2:
                                    q = 2 if p == 1 else 1
                                if p ==0 or p == 4:
                                    q = 4 if p == 0 else 0
                                if recode[x][y][q] == 0:
                                    recode[x][y][q] = id
                                    search_list.append([x, y, q ])
       
                            if p == 0:
                               if y >= 1 and recode[x][y - 1][2] == 0:
                                   recode[x][y - 1][2] = id
                                   search_list.append([x, y - 1, 2])
                            if p == 1:                  
                               if x >= 1 and recode[x - 1][y][3] == 0:
                                   recode[x - 1][y][3] = id
                                   search_list.append([x - 1, y, 3])
                            if p == 2:                  
                               if y + 1 < len(recode[x])  and recode[x][y + 1][0] == 0:
                                   recode[x][y + 1][0] = id
                                   search_list.append([x, y + 1, 0])
                            if p == 3:                  
                               if x + 1 <= len(recode)  and recode[x + 1][y][1] == 0:
                                   recode[x + 1][y][1] = id
                                   search_list.append([x + 1, y, 1])
                  
 
        return id           
