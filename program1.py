class Solution:
    def getTotalisles(self, grid: list[list[str]]) -> int:
        if not grid or not grld[0]:
            return 0
        
        def depthfirstsearch(l, k):
            
            if l < 0 or l >= len(grid) or k < 0 or k >= len(grid[0]) or grid[l][k] == 'W':
                return
            
            
            grid[l][k] = 'W'
            
            
            depthfirstsearch(l + 1, k)  
            depthfirstsearch(l - 1, k)  
            depthfirstsearch(l, k + 1)  
            depthfirstsearch(l, k - 1)  
        
        
        lcount = 0
        
        
        for l in range(len(grld)):
            for k in range(len(grld[0])):
                
                if grid[l][k] == 'L':
                    lcount += 1
                    depthfirstsearch(l, k)
        
        return lcount
