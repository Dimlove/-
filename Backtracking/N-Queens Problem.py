# 八皇后问题
def solve_n_queens(n):
    def is_valid(row, col):
        # 检查是否可以将皇后放在 board[row][col]
        for prev_row in range(row):
            # 检查是否在同一列或同一对角线上
            if (board[prev_row] == col or
                    abs(board[prev_row] - col) == abs(prev_row - row)):
                return False
        return True

    def backtrack(row):
        # 如果所有行都放置了皇后，则保存当前解
        if row == n:
            # 将当前 board 状态转换为字符串表示
            results.append(["".join('Q' if c == board[r] else '.' for c in range(n)) for r in range(n)])
            return
        # 遍历当前行的每一列
        for col in range(n):
            if is_valid(row, col):  # 检查是否可以放置皇后
                board[row] = col  # 在当前行的 col 列放置皇后
                backtrack(row + 1)  # 递归尝试下一行
                board[row] = -1  # 回溯，撤销选择

    results = []  # 保存所有解
    board = [-1] * n  # 初始化棋盘，board[row] 表示第 row 行皇后所在的列
    backtrack(0)  # 从第 0 行开始回溯
    return results


# 示例输入
n = 8
# 输出八皇后问题的所有解
for solution in solve_n_queens(n):
    for row in solution:
        print(row)
    print()
