# 二分查找主函数
def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # 初始化左右指针
    while left <= right:
        mid = (left + right) // 2  # 找到中间索引
        if arr[mid] == target:
            return mid  # 找到目标，返回索引
        elif arr[mid] < target:
            left = mid + 1  # 如果目标大于中间元素，则在右半部分查找
        else:
            right = mid - 1  # 如果目标小于中间元素，则在左半部分查找
    return -1  # 如果目标不存在，返回 -1


# 测试
arr = [3, 9, 10, 27, 38, 43, 82]  # 输入数组必须是有序的
target = 43
print(binary_search(arr, target))  # 输出目标元素的索引，第6个, 输出值为5
