import sys
sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    colors = [list(map(int, input().split())) for _ in range(n)]

    # 1. 10 * 10 상자 만들기
    cnt = [([0] * 10) for i in range(10)]

    # 2. 빨강, 파랑 상자 위치에 cnt 표시!
    for i in range(len(colors)):
        # 빨강
        if colors[i][4] == 1:
            for j in range(colors[i][0], colors[i][2] + 1):
                for k in range(colors[i][1], colors[i][3] + 1):
                    cnt[j][k] += 1 # 빨강과 파랑을 구분

        # 파랑
        elif colors[i][4] == 2:
            for j in range(colors[i][0], colors[i][2] + 1):
                for k in range(colors[i][1], colors[i][3] + 1):
                    cnt[j][k] += 2 # 빨강과 파랑을 구분

    ans = 0
    for i in range(len(cnt)):
        for j in range(len(cnt)):
            if cnt[i][j] > 2: # 합이 3이면 빨강, 파랑 모두 칠한 곳
                ans += 1
    print('#%d %d' % (t, ans))

