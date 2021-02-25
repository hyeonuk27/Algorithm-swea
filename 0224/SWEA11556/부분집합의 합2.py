import sys
sys.stdin = open('input.txt')

A = list(range(1, 13))
AN = 12

def DFS_subset(level, C, S):
    if S > K or C > N: return
    if level == AN:
        if C == N and S == K:
            global sol
            sol += 1
        return

    DFS_subset(level + 1, C + 1, S + A[level])
    DFS_subset(level + 1, C, S)

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    sol = 0
    DFS_subset(0, 0, 0)
    print('#%d %d' % (t, sol))