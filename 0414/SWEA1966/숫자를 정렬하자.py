import sys
sys.stdin = open('input.txt')

def SelectionSort(n, s):
    if s == n-1: return
    min = s
    for i in range(s, n):
        if nums[min] > nums[i]:
            min = i
    nums[s], nums[min] = nums[min], nums[s]
    SelectionSort(n, s+1)

for t in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    SelectionSort(n, 0)
    ans = ' '.join(map(str, nums))
    print('#%d %s' % (t, ans))