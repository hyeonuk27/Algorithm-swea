import sys
sys.stdin = open('input.txt')

def merge_sort(nums):
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    A = merge_sort(nums[mid:])
    B = merge_sort(nums[:mid])
    tmp = []
    a = b = 0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            tmp.append(A[a])
            a += 1
        else:
            tmp.append(B[b])
            b += 1
    tmp.extend(A[a:])
    tmp.extend(B[b:])
    return tmp

for t in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    print('#%d %s' % (t, ' '.join(map(str, merge_sort(nums)))))