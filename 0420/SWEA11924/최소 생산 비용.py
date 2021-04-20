import sys
sys.stdin = open('input.txt')

def get_min_cost(lv, S):
    global min_cost
    if S >= min_cost:
        return
    if lv >= N:
        min_cost = S
        return
    for x in range(N):
        if visit[x]: continue
        visit[x] = 1
        get_min_cost(lv + 1, S + cost[lv][x])
        visit[x] = 0


for t in range(1, int(input()) + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    min_cost = 987654321
    get_min_cost(0, 0)
    print('#%d %d' % (t, min_cost))