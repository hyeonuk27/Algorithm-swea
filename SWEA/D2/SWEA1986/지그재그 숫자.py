import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())

    ans = 0
    cnt = 1
    while cnt < N + 1:
        if cnt % 2:
            ans += cnt
        else:
            ans -= cnt
        cnt += 1

    print('#{} {}'.format(t, ans))