import sys
sys.stdin = open('input.txt')

def perm(idx, sub_sum):
    global ans
    # 가지치기
    if sub_sum > n:
        return

    if idx == 3:
        if sub_sum == n:
            cnt = 0

            st = select[0]
            st2 = st + select[1]

            # 흰색 칠하기
            for i in flag[:st]:
                for j in i:
                    if j != 'W':
                        cnt += 1

            # 파란색 칠하기
            for i in flag[st:st2]:
                for j in i:
                    if j != 'B':
                        cnt += 1

            # 빨간색 칠하기
            for i in flag[st2:]:
                for j in i:
                    if j != 'R':
                        cnt += 1

            if ans > cnt:
                ans = cnt

        return

    # 중복순열 응용
    for i in range(1, n-1):
        select[idx] = i
        perm(idx+1, sub_sum+i)

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    flag = [list(input()) for _ in range(n)]
    select = [0] * 3
    ans = 93248273894

    # 인덱스, 중간 합
    perm(0, 0)
    print('#{} {}'.format(t, ans))