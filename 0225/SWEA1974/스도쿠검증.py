import sys
sys.stdin = open('input.txt')

def check():
    # 가로 세로 체크
    for i in range(9):
        cnt = [0] * (n + 1)
        for j in range(9):
            pos = BRD[i][j]
            cnt[pos] += 1
            if cnt[pos] > 1:
                return 0

        cnt = [0] * (n + 1)
        for j in range(9):
            pos = BRD[j][i]
            cnt[pos] += 1
            if cnt[pos] > 1:
                return 0
    # 3 * 3 체크
    for c in range(0, 9, 3):
        cnt = [0] * (n + 1)
        for i in range(c, c + 3):
            for j in range(c, c + 3):
                pos = BRD[j][i]
                cnt[pos] += 1
                if cnt[pos] > 1:
                    return 0
    return 1

for t in range(1, int(input()) + 1):
    n = 9
    BRD = [list(map(int, input().split())) for _ in range(n)]
    print('#%d %d' % (t, check()))