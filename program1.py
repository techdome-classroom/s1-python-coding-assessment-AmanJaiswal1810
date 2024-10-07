class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        def depthfirstsearch(i, j):
            
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
                return
            
            
            grid[i][j] = 'W'
            
            
            depthfirstsearch(i + 1, j)  # Down
            depthfirstsearch(i - 1, j)  # Up
            depthfirstsearch(i, j + 1)  
            depthfirstsearch(i, j - 1)  
        
        
        icount = 0
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 'L':
                    icount += 1
                    depthfirstsearch(i, j)
        
        return icount
