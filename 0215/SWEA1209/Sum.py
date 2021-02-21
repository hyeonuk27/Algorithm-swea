import sys
sys.stdin = open('input.txt')

# 최대값 반환 함수
def get_max(sum_lst):
    max_sum = 0
    for i in sum_lst:
        if max_sum < i :
            max_sum = i
    return max_sum

for t in range(1, 11):
    tc = int(input())
    n = 100
    space = [list(map(int, input().split())) for _ in range(100)]

    # 네 방향 sum을 담을 리스트 초기화
    sum_lst = []
    # 가로 합, 세로 합 구하기
    for i in range(n):
        raw = 0
        col = 0
        for j in range(n):
            raw += space[i][j]
            col += space[j][i]
        sum_lst += [raw, col]
    # 대각선 합 구하기
    dia1, dia2 = 0, 0
    for i in range(n):
        for j in range(n):
            if i == j:
                dia1 += space[i][j]
            elif i == n - 1 - j:
                dia2 += space[i][n-1-j]
        sum_lst += [dia1, dia2]

        # 네 방향 합 중 최대값 구하기
        ans = get_max(sum_lst)

    print('#%d %d' % (t, ans))




