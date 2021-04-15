import sys
sys.stdin = open('input.txt')

def DFS(lv, c, S):
    global mn
    if S >= mn:
        return
    if lv == N - 1:
        mn = min(mn, S + battery[c][0])
        return
    for i in range(1, N):
        if not check[i]:
            check[i] = 1
            DFS(lv + 1, i, S + battery[c][i])
            check[i] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    check = [1] + [0] * (N - 1)
    mn = 987654321
    DFS(0, 0, 0)
    print("#%d %d" % (t, mn))