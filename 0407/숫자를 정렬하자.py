import sys
sys.stdin = open('input.txt')

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    a = merge_sort(arr[:mid])
    b = merge_sort(arr[mid:])
    temp = []
    ai = bi = 0
    while ai < len(a) and bi < len(b):
        if a[ai] <= b[bi]:
            temp.append(a[ai])
            ai += 1
        else:
            temp.append(b[bi])
            bi += 1
    temp.extend(a[ai:])
    temp.extend(b[bi:])
    return temp

for t in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = ' '.join(map(str, merge_sort(nums)))
    print('#%d %s' % (t, ans))