import sys
sys.stdin = open('input.txt')

def get_maxP(lv, tot):
    global maxP
    if maxP >= tot:
        return
    if tot == 0:
        return
    if lv >= N:
        maxP = tot
        return
    for j in range(N):
        if V[j]: continue
        V[j] = 1
        get_maxP(lv + 1, tot * P[lv][j] / 100)
        V[j] = 0

ans = []
for t in range(1, int(input())+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    V = [0] * N
    maxP = 0
    get_maxP(0, 1)
    ans.append('#%s %.6f' % (t, maxP * 100))
print('\n'.join(ans))