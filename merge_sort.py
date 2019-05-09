'''
时间复杂度：O(n log(n))
空间复杂度：O(n)
是否稳定：是
使用场景：数据量较大且要求排序稳定时
'''


def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c


def merge_sort(lists):

    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


if __name__ == '__main__':
    list_data = [92,0,43,-12,23,80,14]
    result = merge_sort(list_data)
    print(result)