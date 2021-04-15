import sys
sys.stdin = open('input.txt')

def perm(n, k):
    global ans
    if k == n:
        route = [1] + a + [1]
        tot = [grid[route[i]][route[i+1]] for i in range(n + 1)]
        ans = min(ans, sum(tot))
    for i in range(k, n):
        a[i], a[k] = a[k], a[i]
        perm(n, k + 1)
        a[i], a[k] = a[k], a[i]

for t in range(1, int(input())+1):
    N = int(input())
    grid = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    a = list(range(2, N + 1))
    ans = 987654321
    perm(N - 1, 0)
    print('#%d %d' % (t, ans))