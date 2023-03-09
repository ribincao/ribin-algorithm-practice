class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.check(board, True):
            return False
        if not self.check(board, False):
            return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                tmp = []
                tmp.extend(board[i][j:j + 3])
                tmp.extend(board[i + 1][j:j + 3])
                tmp.extend(board[i + 2][j:j + 3])
                if not self.check([tmp]):
                    return False

        return True

    def check(self, board: List[List[str]], row: bool = True) -> bool:
        n = len(board)
        m = len(board[0])
        for i in range(n):
            Founded = set()
            for j in range(m):
                if row:
                    c = board[i][j]
                else:
                    c = board[j][i]
                if c != '.':
                    if c in Founded:
                        return False
                    Founded.add(c)
        return True