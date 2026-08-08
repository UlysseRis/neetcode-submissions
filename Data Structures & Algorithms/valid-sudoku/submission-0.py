class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            h_row = set()
            for j in range(n):
                inter = board[i][j]
                if inter != '.':
                    num = int(inter)
                    if num in h_row:
                        return False
                    h_row.add(num)

        for i in range(n):
            h_col = set()
            for j in range(n):
                inter = board[j][i]
                if inter != '.':
                    num = int(inter)
                    if num in h_col:
                        return False
                    h_col.add(num)

        m = int(n/3)
        for i in range(m):
            for j in range(m):
                h_square = set()
                for k in range(3):
                    for l in range(3):
                        inter = board[3*i+k][3*j+l]
                        if inter != '.':
                            num =int(inter)
                            if num in h_square:
                                return False
                            h_square.add(num)
        return True
