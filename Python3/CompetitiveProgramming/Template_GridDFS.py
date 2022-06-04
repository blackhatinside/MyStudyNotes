class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        m = len(grid)
        n = len(grid[0])
        notvisited = 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j # starting square found
                elif grid[i][j] == 0:
                    notvisited += 1 # empty square found
        
        def isvalid(x, y):
            return (0 <= x < m and 0 <= y < n and grid[x][y] >= 0)
        
        def dfs(x, y, notvisited):
            if not isvalid(x, y):
                return
            if grid[x][y] == 2: # if ending square
                if notvisited == 0:
                    self.ans += 1
                return
            grid[x][y] = -2 # mark visited
            dfs(x - 1, y, notvisited - 1)    # left
            dfs(x + 1, y, notvisited - 1)    # right
            dfs(x, y - 1, notvisited - 1)    # up
            dfs(x, y + 1, notvisited - 1)    # down
            grid[x][y] = 0  # unmark visited
    
        dfs(x, y, notvisited)
        return self.ans

'''---------- https://leetcode.com/problems/unique-paths-iii/ ----------'''
        
class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
    # def solve(self, grid: List[List[str]]) -> None:
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
            return (0 <= x < m and 0 <= y < n and grid[x][y] >= 0)
            # return (0 <= x < m and 0 <= y < n)
        
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
        dfs1(x, y, notvisited)

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
                    # dfs2(i, j)
                    islandcount += 1
          
        def dfs3(x, y):
            if not isvalid(x, y):
                return
            if grid[x][y] == "X" or grid[x][y] == "Y": # if ending square
                return
            grid[x][y] = "Y" # mark visited
            dfs3(x - 1, y)    # left
            dfs3(x + 1, y)    # right
            dfs3(x, y - 1)    # up
            dfs3(x, y + 1)    # down
            return
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    if grid[i][j] == "O":
                        # dfs3(i, j)
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "O":
        #             grid[i][j] = "X"
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "Y":
        #             grid[i][j] = "O"

        return self.ans
        # return islandcount
        
'''---------- https://leetcode.com/problems/number-of-islands/ ----------'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    # def uniquePathsIII(self, grid: List[List[int]]) -> int:
    # def solve(self, grid: List[List[str]]) -> None:
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
          
        def dfs3(x, y):
            if not isvalid(x, y):
                return
            if grid[x][y] == "X" or grid[x][y] == "Y": # if ending square
                return
            grid[x][y] = "Y" # mark visited
            dfs3(x - 1, y)    # left
            dfs3(x + 1, y)    # right
            dfs3(x, y - 1)    # up
            dfs3(x, y + 1)    # down
            return
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    if grid[i][j] == "O":
                        dfs3(i, j)
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "O":
        #             grid[i][j] = "X"
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "Y":
        #             grid[i][j] = "O"

        # return self.ans
        return islandcount

'''---------- https://leetcode.com/problems/surrounded-regions/ ----------'''

class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    # def uniquePathsIII(self, grid: List[List[int]]) -> int:
    def solve(self, grid: List[List[str]]) -> None:
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
                    # dfs2(i, j)
                    islandcount += 1
          
        def dfs3(x, y):
            if not isvalid(x, y):
                return
            if grid[x][y] == "X" or grid[x][y] == "Y": # if ending square
                return
            grid[x][y] = "Y" # mark visited
            dfs3(x - 1, y)    # left
            dfs3(x + 1, y)    # right
            dfs3(x, y - 1)    # up
            dfs3(x, y + 1)    # down
            return
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    if grid[i][j] == "O":
                        dfs3(i, j)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "O":
                    grid[i][j] = "X"
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "Y":
                    grid[i][j] = "O"

        # return self.ans
        # return islandcount
