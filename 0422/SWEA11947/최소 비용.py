import sys
sys.stdin = open('input.txt')

drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS():
    q = [(0, 0)]
    fuel = [[987654321] * N for _ in range(N)]
    fuel[0][0] = 0
    while q:
        r, c = q.pop(0)
        for dr, dc in drc:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N:
                tmp = (grid[nr][nc] - grid[r][c]) if grid[nr][nc] > grid[r][c] else 0
                fill = fuel[r][c] + 1 + tmp
                if fuel[nr][nc] > fill:
                    fuel[nr][nc] = fill
                    q.append((nr, nc))
    return fuel[-1][-1]

for t in range(1, int(input())+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    print('#%d %d' % (t, BFS()))