'''
平均情况：O(n^2)
最好情况：O(n^2)
最坏情况：O(n^2)
辅助空间：O(1)
是否稳定：是
使用场景：当数据规模较小时，选择排序性能较好
'''


def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


if __name__ == '__main__':
    list_data = [92, 0, 43, -12, 23, 80, 14]
    result = selection_sort(list_data)
    print(result)
