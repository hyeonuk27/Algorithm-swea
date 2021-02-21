import sys
sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    nums = list(map(int, input().split()))

    max_idx, min_idx = 0, 0
    for i in range(n):
        if nums[max_idx] <= nums[i]:
            max_idx = i
        if nums[min_idx] > nums[i]:
            min_idx = i

    ans = abs(max_idx - min_idx)

    print('#{} {}'.format(t, ans))
