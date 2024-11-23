# 数独
def solve_sudoku(board):
    def is_valid(row, col, num):
        # 检查行中是否已经存在 num
        if num in board[row]:
            return False
        # 检查列中是否已经存在 num
        if any(board[i][col] == num for i in range(9)):
            return False
        return True  # 如果满足行和列的要求，则合法

    def backtrack():
        # 遍历整个棋盘，寻找空白格子
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':  # 如果是空白格子
                    # 尝试填入数字 1 到 9
                    for num in map(str, range(1, 10)):
                        if is_valid(row, col, num):  # 检查当前数字是否合法
                            board[row][col] = num  # 填入数字
                            if backtrack():  # 递归解决剩余问题
                                return True
                            board[row][col] = '.'  # 回溯，撤销选择
                    return False  # 如果无法填入任何数字，返回失败
        return True  # 所有格子都已填满，返回成功

    backtrack()  # 开始回溯
    return board

# 示例输入（去掉了子网格检查的棋盘）
sudoku_board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

# 输出解
print(solve_sudoku(sudoku_board))
