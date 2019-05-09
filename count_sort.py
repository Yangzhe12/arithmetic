'''
时间复杂度：O(n)
空间复杂度：O(n)+O(N)
是否稳定：是
使用场景：计数排序虽然时间复杂度较低，但需要满足的条件较多，如果能满足限制条件与空间需求，计数排序自然很快
'''


def count_sort(arr):
    n = len(arr)
    res = [None] * n
    for i in range(n):
        p = 0
        q = 0
        for j in range(n):
            if arr[i] > arr[j]:
                p += 1
            elif arr[i] == arr[j]:
                q += 1
        for k in range(p, p+q):
            res[k] = arr[i]
    return res


if __name__ == '__main__':
    list_data = [92,0,43,-12,23.5,80,14]
    result = count_sort(list_data)
    print(result)