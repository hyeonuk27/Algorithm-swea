import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    nums = list(map(int, input().split()))

    max_num, min_num = 0, 10000
    for i in nums:
        if max_num < i:
            max_num = i
        if min_num > i:
            min_num = i

    my_sum = cnt = 0
    for j in nums:
        if j != max_num and j != min_num:
            my_sum += j
            cnt += 1

    ans = round(my_sum / cnt)
    print('#{} {}'.format(t, ans))