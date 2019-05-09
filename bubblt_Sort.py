'''
时间复杂度：O(n^2)
空间复杂度：原址排序
是否稳定：是
使用场景：规模比较小时使用冒泡
'''


def bubblt_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    list_data = [8, -92, 3, 56, 32, -65, -1, 67, 45]
    result = bubblt_sort(list_data)
    print(result)