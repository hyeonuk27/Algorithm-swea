import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    flag = [input() for _ in range(n)]

    W = [0] * n
    B = [0] * n
    R = [0] * n

    # 행을 보면서 나와 다른 색깔의 개수를 카운팅
    for i in range(n):
        for j in range(m):
            if flag[i][j] != 'W':
                W[i] += 1
            if flag[i][j] != 'B':
                B[i] += 1
            if flag[i][j] != 'R':
                R[i] += 1

    # 누적합
    for i in range(1, n):
        W[i] += W[i-1]
        B[i] += B[i-1]
        R[i] += R[i-1]

    ans = 94587593

    # 각각의 색 별로 한 줄씩 이상은 확보해야하므로
    for i in range(n-2):
        for j in range(i+1, n-1):
            w_cnt = W[i]
            b_cnt = B[j] - B[i]
            r_cnt = R[n-1] - R[j]

            if ans > w_cnt + b_cnt + r_cnt:
                ans =  w_cnt + b_cnt + r_cnt

    print('#{} {}'.format(t, ans))