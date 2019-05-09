'''
时间复杂度：O(n log(n))
空间复杂度：原址排序
是否稳定：否
使用场景：堆排序适合处理数据量大的情况，数据呈流式输入时用堆排序也很方便
'''


def build_heap(arr):
    length = len(arr)
    index = int(length/2) - 1
    for i in range(index, -1, -1):
        heapify(arr, index)


def heapify(arr,index):
    if index > len(arr) / 2 - 1:
        return None
    max_index = index
    left_child_index = index * 2 + 1
    right_child_index = index * 2 + 2
    if left_child_index < len(arr) and arr[left_child_index] > arr[max_index]:
        max_index = left_child_index
    if right_child_index < len(arr) and arr[right_child_index] > arr[max_index]:
        max_index = right_child_index
    if arr[max_index] != arr[index]:
        arr[max_index], arr[index] = arr[index], arr[max_index]
        heapify(arr,max_index)


def heap_sort(arr):
    arr_sorted = []
    build_heap(arr)
    while len(arr) != 0:
        temp = arr[0]
        arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]
        arr_sorted.insert(0, arr.pop(len(arr) - 1))
        heapify(arr,0)
    return arr_sorted


if __name__ == '__main__':
    list_data = [92,0,43,-12,23,80,14]
    result = heap_sort(list_data)
    print(result)