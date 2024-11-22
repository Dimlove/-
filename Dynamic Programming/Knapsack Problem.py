# 0/1 背包问题的动态规划实现
def knapsack(weights, values, capacity):
    n = len(weights)

    # 初始化dp数组，dp[i][w]表示前i个物品，容量为w时的最大价值
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 填充dp数组
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:  # 如果当前物品可以放入背包
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]  # 不放当前物品

    return dp[n][capacity]


# 测试
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print("Knapsack Max Value =", knapsack(weights, values, capacity))  # 输出最大价值
