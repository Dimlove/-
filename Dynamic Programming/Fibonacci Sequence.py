# 斐波那契数列的动态规划实现
def fibonacci(n):
    if n <= 1:
        return n

    # 初始化dp数组
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1  # 基础情况

    # 填充dp数组
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# 测试
n = 10
print(f"Fibonacci({n}) =", fibonacci(n))  # 输出斐波那契数列的第n项
