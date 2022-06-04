class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#     def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        m = len(grid)
        n = len(grid[0])
        notvisited = 1
        islandcount = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j # starting square found
                elif grid[i][j] == 0:
                    notvisited += 1 # empty square found
        
        def isvalid(x, y):
            # return (0 <= x < m and 0 <= y < n and grid[x][y] >= 0)
            return (0 <= x < m and 0 <= y < n)
        
        def dfs1(x, y, notvisited):
            if not isvalid(x, y):
                return
            if grid[x][y] == 2: # if ending square
                if notvisited == 0:
                    self.ans += 1
                return
            grid[x][y] = -2 # mark visited
            dfs1(x - 1, y, notvisited - 1)    # left
            dfs1(x + 1, y, notvisited - 1)    # right
            dfs1(x, y - 1, notvisited - 1)    # up
            dfs1(x, y + 1, notvisited - 1)    # down
            grid[x][y] = 0  # unmark visited
        # dfs1(x, y, notvisited)

        def dfs2(x, y):
            if not isvalid(x, y):
                return
            if grid[x][y] == "0": # if ending square
                return
            grid[x][y] = "0"    # mark visited
            dfs2(x - 1, y)      # left
            dfs2(x + 1, y)      # right
            dfs2(x, y - 1)      # up
            dfs2(x, y + 1)      # down
            return
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs2(i, j)
                    islandcount += 1

        # return self.ans
        return islandcount
