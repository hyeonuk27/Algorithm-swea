import sys
sys.stdin = open('input.txt')

def quick_sort(left, right):
    if left >= right:
        return
    i, p = left, right
    for j in range(left, right):
        if nums[j] < nums[p]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[p] = nums[p], nums[i]
    quick_sort(left, i-1)
    quick_sort(i+1, right)


for t in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    quick_sort(0, n-1)
    print('#%d %d' % (t, nums[n//2]))
