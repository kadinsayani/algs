# O(m*n)
# using dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])
        ans = 0
        visited = set()

        def dfs(i, j):
            visited.add((i, j))
            for x, y in [[i+1, j], [i, j+1], [i-1, j], [i, j-1]]:
                if x in range(m) and y in range(n) and (x, y) not in visited and grid[x][y] == "1":
                    dfs(x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    ans += 1
                    dfs(i, j)

        return ans
