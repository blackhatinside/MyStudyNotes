class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        notvisited = 1  # taking source node into account

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j # starting square found
                elif grid[i][j] == 0:
                    notvisited += 1 # empty square found

        def isvalid(x, y):  # edges and blockage conditions
            return (0 <= x < m and 0 <= y < n and grid[x][y] >= 0)

        def dfs(x, y, notvisited):
            nonlocal ans
            if not isvalid(x, y):
                return
            if grid[x][y] == 2: # if ending square
                if notvisited == 0:
                    ans += 1
                return
            grid[x][y] = -2 # mark visited
            dfs(x - 1, y, notvisited - 1)    # left
            dfs(x + 1, y, notvisited - 1)    # right
            dfs(x, y - 1, notvisited - 1)    # up
            dfs(x, y + 1, notvisited - 1)    # down
            grid[x][y] = 0  # unmark visited

        ans = 0
        dfs(x, y, notvisited)
        return ans



'''---------- https://leetcode.com/problems/flood-fill/ ----------'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        srcColor = image[sr][sc]
        m, n = len(image), len(image[0])

        def fill(x, y):
            if x < 0 or x >= m:     # boundary check
                return
            if y < 0 or y >= n:     # boundary check
                return
            if image[x][y] != srcColor:
                return
            if image[x][y] == newColor:
                return
            image[x][y] = newColor
            fill(x + 1, y)  # right
            fill(x - 1, y)  # left
            fill(x, y + 1)  # up
            fill(x, y - 1)  # down

        fill(sr, sc)
        return image

'''---------- https://leetcode.com/problems/unique-paths-iii/ ----------'''

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        notvisited = 1  # taking source node into account

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j # starting square found
                elif grid[i][j] == 0:
                    notvisited += 1 # empty square found

        def isvalid(x, y):  # edges and blockage conditions
            return (0 <= x < m and 0 <= y < n and grid[x][y] >= 0)

        def dfs(x, y, notvisited):
            nonlocal ans
            if not isvalid(x, y):
                return
            if grid[x][y] == 2: # if ending square
                if notvisited == 0:
                    ans += 1
                return
            grid[x][y] = -2 # mark visited
            dfs(x - 1, y, notvisited - 1)    # left
            dfs(x + 1, y, notvisited - 1)    # right
            dfs(x, y - 1, notvisited - 1)    # up
            dfs(x, y + 1, notvisited - 1)    # down
            grid[x][y] = 0  # unmark visited

        ans = 0
        dfs(x, y, notvisited)
        return ans

'''---------- https://leetcode.com/problems/number-of-islands/ ----------'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        notvisited = 1  # taking source node into account

        def isvalid(x, y):  # edges and blockage conditions
            return (0 <= x < m and 0 <= y < n and grid[x][y] == "1")

        def dfs(x, y):
            if not isvalid(x, y):
                return
            grid[x][y] = "0" # mark visited
            dfs(x - 1, y)    # left
            dfs(x + 1, y)    # right
            dfs(x, y - 1)    # up
            dfs(x, y + 1)    # down
            # grid[x][y] = 0  # no need to unmark visited
            return

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":   # if land
                    dfs(i, j)
                    ans += 1
        return ans

'''---------- https://leetcode.com/problems/surrounded-regions/ ----------'''

class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        m, n = len(grid), len(grid[0])

        def isvalid(x, y):  # edges and blockage conditions
            return (0 <= x < m and 0 <= y < n and grid[x][y] == "O")

        def dfs(x, y):
            if not isvalid(x, y):
                return
            grid[x][y] = "Y" # mark visited
            dfs(x - 1, y)    # left
            dfs(x + 1, y)    # right
            dfs(x, y - 1)    # up
            dfs(x, y + 1)    # down
            # grid[x][y] = 0  # no need to unmark visited
            return

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "O" and (i == 0 or i == m - 1 or j == 0 or j == n - 1):   # if land
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "O":
                    grid[i][j] = "X"
                if grid[i][j] == "Y":
                    grid[i][j] = "O"                    
        return grid

'''---------- https://leetcode.com/problems/count-sub-islands/ ----------'''

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        def check(x, y):
            if x < 0 or x >= m:     # boundary - dfs finished without errors
                return 0
            if y < 0 or y >= n:     # boundary - dfs finished without errors
                return 0
            if grid2[x][y] == 0:    # already visited - dfs finished without errors
                return 0
            return 1
        def fill(x, y):
            if check(x, y) == 0:
                return 1
            if grid2[x][y] == 1 and grid1[x][y] == 0:   # land missing in grid1 - invalid dfs
                return 0
            grid2[x][y] = 0         # make visited
            res = fill(x + 1, y) & fill(x - 1, y) & fill(x, y + 1) & fill(x, y - 1)
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 1 and grid2[i][j] == 1:
                    ans += fill(i, j) > 0   # condition for valid island - should finish dfs path fully
        return ans

'''---------- https://leetcode.com/problems/max-area-of-island/ ----------'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        globalmaxarea = 0

        def fill(x, y):
            nonlocal localmaxarea
            if x < 0 or x >= m:     # boundary check
                return 0
            if y < 0 or y >= n:     # boundary check
                return 0
            if grid[x][y] == 0:     # already visited
                return 0
            grid[x][y] = 0  # mark visited
            ans = 1
            for i in range(1):
                ans += fill(x + 1, y)   # right
                ans += fill(x - 1, y)   # left
                ans += fill(x, y + 1)   # up
                ans += fill(x, y - 1)   # down
            return ans

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    localmaxarea = fill(i, j)
                    globalmaxarea = max(globalmaxarea, localmaxarea)
        return globalmaxarea

'''---------- https://leetcode.com/problems/island-perimeter/ ----------'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        px, py = -1, -1
        found = False

        for i in range(m):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    px, py = i, j
                    found = True
                    break

        peri = 0
        def fill(x, y):
            nonlocal peri
            if x < 0 or x >= m:     # outer boundary - add to perimeter
                peri += 1
                return
            if y < 0 or y >= n:     # outer boundary - add to perimeter
                peri += 1
                return
            if grid[x][y] == 0:     # inner boundary - add to perimeter
                peri += 1
                return
            if grid[x][y] == 2:     # already visited
                return
            grid[x][y] = 2          # mark visited
            fill(x + 1, y)  # right
            fill(x - 1, y)  # left
            fill(x, y + 1)  # up
            fill(x, y - 1)  # down
        fill(px, py)
        return peri
