import sys
sys.stdin = open('input.txt')

def merge_sort(nums):
    global cnt
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    A = merge_sort(nums[:mid])
    B = merge_sort(nums[mid:])
    if A[-1] > B[-1]:
        cnt += 1
    tmp = []
    ai = bi = 0
    while ai < len(A) and bi < len(B):
        if A[ai] <= B[bi]:
            tmp.append(A[ai])
            ai += 1
        else:
            tmp.append(B[bi])
            bi += 1
    tmp.extend(A[ai:])
    tmp.extend(B[bi:])
    return tmp

for t in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(nums)[n//2]
    print('#%d %d %d' % (t, ans, cnt))
