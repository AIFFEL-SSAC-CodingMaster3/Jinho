class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #count island
        island_cnt = 0
        row_len = len(grid)
        col_len = len(grid[0])
        visited = [ [False]* col_len for _ in range(row_len) ]
        
        def dfs(x,y):            
            if row_len > x >= 0 and col_len > y >= 0 and not visited[x][y]:
                visited[x][y] = True                
                if grid[x][y] == '1':
                    return dfs(x+1, y) +  dfs(x, y+1) +  dfs(x-1, y) +  dfs(x, y-1)
                else:
                    return 0
            else:
                return 0
        
        for row in range(row_len):
            for col in range(col_len):
                if not visited[row][col]:
                    if grid[row][col] == '1':
                        dfs(row,col)
                        island_cnt += 1
                    else:
                        visited[row][col] = True
                        
        return island_cnt