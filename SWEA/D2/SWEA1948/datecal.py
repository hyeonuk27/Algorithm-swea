import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    date = list(map(int, input().split())) # [2, 13, 6, 12]

    # 월 마지막 날짜
    last_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # [1] 1/1 ~ 3/31 날짜 세기
    long_date = 0
    for i in range(0, date[2]-1):
        long_date += last_date[i]
    first_sum = long_date + date[3]

    # [2] 1/1 ~ 3/1 날짜 세기
    short_date = 0
    for j in range(0, date[0]-1):
        short_date += last_date[j]
    second_sum = short_date + date[1]


    # [1] - [2] + 1

    ans = first_sum - second_sum + 1

    print('#{} {}'.format(tc, ans))









