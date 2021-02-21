import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    nums = list(map(int, input().split()))

    cnt = 0
    sum_nums = 0
    for i in range(len(nums)):
        sum_nums += nums[i]
        cnt += 1

    ans = round(sum_nums/cnt)

    print('#{} {}'.format(tc, ans))