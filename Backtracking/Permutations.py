# 全排列
def permute(nums):
    def backtrack(path, used):
        # 如果路径长度等于 nums 的长度，则找到一个完整排列
        if len(path) == len(nums):
            results.append(path[:])  # 保存当前路径
            return
        # 遍历所有数字，尝试将每个数字加入路径
        for i in range(len(nums)):
            if not used[i]:  # 检查数字是否已经使用过
                used[i] = True  # 标记为已使用
                path.append(nums[i])  # 将数字加入路径
                backtrack(path, used)  # 递归寻找下一个数字
                path.pop()  # 回溯，撤销选择
                used[i] = False  # 撤销标记

    results = []  # 保存所有排列结果
    backtrack([], [False] * len(nums))  # 开始回溯
    return results


# 示例输入
nums = [1, 2, 3]
# 输出所有排列
print(permute(nums))
