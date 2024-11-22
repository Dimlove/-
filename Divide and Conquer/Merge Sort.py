# 归并排序
# 合并两个有序的子数组
def merge(left, right):
    result = []
    i = j = 0
    # 逐个比较两个子数组的元素，按顺序合并
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 如果有剩余元素，直接加入结果中
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 归并排序主函数
def merge_sort(arr):
    # 基本情况：只有一个元素或者空数组
    if len(arr) <= 1:
        return arr
    # 分治：分成两半，递归排序
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # 合并排序好的子数组
    return merge(left, right)


# 测试
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))  # 输出排序后的数组
