import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    tn = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]


    max_row_sum = 0
    max_col_sum = 0
    # 가로 합, 세로 합, 대각선 합
    for i in range(len(arr)):
        row_sum = 0
        col_sum = 0
        diagonal_sum1 = 0
        diagonal_sum2 = 0
        for j in range(len(arr)-1, -1, -1):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
            diagonal_sum1 += arr[i][j]
            diagonal_sum2 += arr[j][j]
        # 가로 합, 세로 합 -> 최대값 구하기
        if max_row_sum < row_sum:
            max_row_sum = row_sum
        if max_col_sum < col_sum:
            max_col_sum = col_sum

    # 가로 합기 최대값, 세로 합 최대값, 대각선 합 -> 최대값 구하기
    max_ans = 0
    ans = [max_row_sum, max_col_sum, diagonal_sum1, diagonal_sum2]
    for k in ans:
        if max_ans < k:
            max_ans = k
    print('#{} {}'.format(t, max_ans))


