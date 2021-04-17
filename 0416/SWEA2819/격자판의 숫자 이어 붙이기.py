import sys
sys.stdin = open('input.txt')

drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_line(n, r, c, line):
    if n == 7:
        lines.add(line)
        return
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            get_line(n+1, nr, nc, line + grid[nr][nc])


for t in range(1, int(input())+1):
    grid = [input().split() for _ in range(4)]
    lines = set()
    for r in range(4):
        for c in range(4):
            get_line(1, r, c, grid[r][c])
    print('#%d %d' % (t, len(lines)))