class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        box_columns = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                box_index = (i//3) * 3 + (j//3)
                if value in rows[i] or value in columns[j] or value in box_columns[box_index]:
                    return False
                rows[i].add(value)
                columns[j].add(value)
                box_columns[box_index].add(value)
        return True