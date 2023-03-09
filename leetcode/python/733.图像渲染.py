class Solution:
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        ori = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        n, m = len(image), len(image[0])
        ret = []

        def dfs(r, c):
            if r < 0 or r >= n:
                return
            if c < 0 or c >= m:
                return
            if image[r][c] == color and [r, c] not in ret:
                image[r][c] = newColor
                ret.append([r, c])
                for o in ori:
                    nr, nc = r + o[0], c + o[1]
                    dfs(nr, nc)
        dfs(sr, sc)
        return image