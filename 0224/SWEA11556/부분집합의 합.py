import sys
sys.stdin = open('input.txt')

A =  list(range(1, 13))
AN = 12
subset = [0] * AN


def get_sum(sub):
    tot = 0
    for i in range(AN):
        if subset[i]:
            tot += A[i]
    return tot


def DFS_subset(level):
    if level == AN:
        if sum(subset) == N and get_sum(subset) == K:
            global sol
            sol += 1
        return

    subset[level] = 1
    DFS_subset(level + 1)
    subset[level] = 0
    DFS_subset(level + 1)


for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    sol = 0
    DFS_subset(0)
    print('#%d %d' % (t, sol))