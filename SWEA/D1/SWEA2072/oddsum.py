import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    nums = list(map(int, input().split()))

    cnt = 0
    while cnt < len(nums):
        cnt += 1
        ans = 0
        for i in range(len(nums)):
            if nums[i] % 2:
                ans += nums[i]

    print('#{} {}'.format(tc, ans) )




