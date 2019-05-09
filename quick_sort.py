'''
时间复杂度：O(n log(n))
空间复杂度：原址排序
是否稳定：否
使用场景：快速排序适合处理大量数据排序时的场景
'''

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    list_data = [8,-92,3,56,32,-65,-1,67,45]
    result = quicksort(list_data)
    print(result)