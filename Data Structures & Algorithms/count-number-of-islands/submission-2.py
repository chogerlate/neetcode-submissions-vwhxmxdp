class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])

        
        def bfs(row, col):
            q = deque()
            q.append((row,col))
            grid[row][col] = "0"
            action = [(1,0),(-1,0),(0,1),(0,-1)]
            while q :
                r, c = q.popleft()
                for ar, ac in action :
                    sr = r + ar
                    sc = c + ac    
                    if 0 <= sr < rows and 0 <= sc < cols and grid[sr][sc] == "1" :
                        q.append((sr,sc))
                        grid[sr][sc] = "0"

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" :
                    res +=1 
                    bfs(row,col)
        return res