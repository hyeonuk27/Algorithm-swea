import sys
sys.stdin = open('input.txt')

for t in range (1, int(input())+1):
    nums = list(map(int, input().split()))
    n = len(nums)

    for i in range(1, 1 << n):
        subset_sum = 0
        for j in range(n):
            if i & (1 << j):
                subset_sum += nums[j]

        if subset_sum == 0:
            print('#%d 1' % t)
            break
    else:
        print('#%d 0' % t)