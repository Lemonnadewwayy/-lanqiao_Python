def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 最后 i 个元素已经排好序，不需要再比较
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换元素位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 测试
arr = [5, 3, 8, 4, 2]
sorted_arr = bubble_sort(arr)
print(sorted_arr)  # 输出: [2, 3, 4, 5, 8]
