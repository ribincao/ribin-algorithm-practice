class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ori = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        ret = []
        start = 0

        def dfs(r, c):
            if r < 0 or r >= n:
                return
            if c < 0 or c >= m:
                return

            if grid[r][c] == 1 and [r, c] not in ret:
                ret.append([r, c])
                for o in ori:
                    nr, nc = r + o[0], c + o[1]
                    dfs(nr, nc)

        cnt = 0
        for sr in range(n):
            for sc in range(m):
                if grid[sr][sc] == 1 and [sr, sc] not in ret:
                    dfs(sr, sc)
                    cnt = max(cnt, len(ret) - start)
                    start = len(ret)
        return cnt