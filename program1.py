class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        def depthfirstsearch(i, k):
            
            if i < 0 or i >= len(grid) or k < 0 or k >= len(grid[0]) or grid[i][k] == 'W':
                return
            
            
            grid[i][k] = 'W'
            
            
            depthfirstsearch(i + 1, k)  
            depthfirstsearch(i - 1, k)  
            depthfirstsearch(i, k + 1)  
            depthfirstsearch(i, k - 1)  
        
        
        icount = 0
        
        
        for i in range(len(grid)):
            for k in range(len(grid[0])):
                
                if grid[i][k] == 'L':
                    icount += 1
                    depthfirstsearch(i, k)
        
        return icount
