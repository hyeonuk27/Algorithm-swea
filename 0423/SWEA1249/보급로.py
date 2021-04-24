import sys
sys.stdin = open('input.txt')

drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS():
    q = [(0, 0)]
    h = [[987654321] * N for _ in range(N)]
    h[0][0] = 0
    while q:
        r, c = q.pop(0)
        for dr, dc in drc:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N:
                S = h[r][c] + grid[nr][nc]
                if h[nr][nc] > S:
                    h[nr][nc] = S
                    q.append((nr, nc))
    return h[-1][-1]


for t in range(1, int(input())+1):
    N = int(input())
    grid = [list(map(int, input())) for _ in range(N)]
    print('#%d %d' % (t, BFS()))