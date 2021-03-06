import sys
sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    cnt = [([0] * 10) for i in range(10)]

    # 주어진 정보에서 같은 색인 영역은 겹치지 않는다 -> 색 구분 불필요
    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
            for j in range(r1, r2 + 1):
                for k in range(c1, c2 +2:
                    cnt[j][k] += 1
    ans = 0
    for i in range(len(cnt)):
        for j in range(len(cnt)):
            if cnt[i][j] == 2:
                ans += 1
    print('#%d %d' % (t, ans))