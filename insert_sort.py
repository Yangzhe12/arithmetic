'''
时间复杂度：O(n^2)
空间复杂度：原址排序
是否稳定：是
使用场景：规模比较小时
'''

def insertion_sort(array):
    for index in range(1, len(array)):
        current_val = array[index]
        position = index
        while position > 0 and (array[position - 1] > current_val):
            array[position] = array[position - 1]
            position -= 1
        array[position] = current_val
    return array

if __name__ == '__main__':
    list_data = [92,77,-43,54,23,80,14]
    result = insertion_sort(list_data)
    print(result)