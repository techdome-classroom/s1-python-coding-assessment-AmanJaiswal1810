class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        def dfs(i, j):
            
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
                return
            
            
            grid[i][j] = 'W'
            
            # Explore all four directions
            dfs(i + 1, j)  # Down
            dfs(i - 1, j)  # Up
            dfs(i, j + 1)  # Right
            dfs(i, j - 1)  # Left
        
        # Initialize island count
        island_count = 0
        
        # Iterate through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Start a DFS for each new island found
                if grid[i][j] == 'L':
                    island_count += 1
                    dfs(i, j)
        
        return island_count
