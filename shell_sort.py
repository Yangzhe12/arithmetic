'''
时间复杂度：小于O(n ^ (4/3))
空间复杂度：原址排序
是否稳定：否
使用场景：数据量较小且基本有序时
'''


def insert_sort(list, step):
    for i in range(step, len(list)):
        for j in range(i, step - 1, -step):
            if list[j] < list[j - step]:
                list[j], list[j - step] = list[j - step], list[j]
            else:
                break


def shell_sort(list):
    length = len(list)
    step = 1
    while step < length // 2:
        step = 2 * step + 1
    while step >= 1:
        insert_sort(list,step)
        step = step // 2
    return list


if __name__ == '__main__':
    list_data = [92,0,43,-12,23,80,14]
    result = shell_sort(list_data)
    print(result)