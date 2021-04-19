import sys
sys.stdin = open('input.txt')

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    A = merge_sort(arr[:mid])
    B = merge_sort(arr[mid:])
    tmp = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(B[j])
            j += 1
    tmp.extend(A[i:])
    tmp.extend(B[j:])
    return tmp

for t in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = ' '.join(map(str, merge_sort(nums)))
    print('#%d %s' % (t, ans))