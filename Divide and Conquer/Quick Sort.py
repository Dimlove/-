# 快速排序主函数
def quick_sort(arr):
    # 基本情况：数组为空或只有一个元素
    if len(arr) <= 1:
        return arr
    # 选择基准元素，这里选择第一个元素
    pivot = arr[0]
    # 分成两部分：小于基准的部分和大于等于基准的部分
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    # 递归排序两部分，并返回结果
    return quick_sort(left) + [pivot] + quick_sort(right)


# 测试
arr = [38, 27, 43, 3, 9, 82, 10]
print(quick_sort(arr))  # 输出排序后的数组
