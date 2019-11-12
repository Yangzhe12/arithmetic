'''
平均情况：O(n^2)
最好情况:(优化后) O(n)
最坏情况：O(n^2)
辅助空间：O(1)
是否稳定：是
使用场景：规模比较小时使用冒泡
'''


def bubblt_sort(array):
    for i in range(len(array)):
        # 添加flag，如果此处循环没有交换发生，则返回
        flag = True
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                flag = False
                array[j], array[j + 1] = array[j + 1], array[j]
        if flag:
            return array
    return array


if __name__ == '__main__':
    list_data = [8, -92, 3, 56, 32, -65, -1, 67, 45]
    result = bubblt_sort(list_data)
    print(result)