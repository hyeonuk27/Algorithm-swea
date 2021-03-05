import sys
sys.stdin = open('input.txt')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(sr, sc):
    visited[sr][sc] = 1
    q.append((sr, sc))
    while q:
        tr, tc = q.pop(0)
        for d in range(4):
            nr = tr + dr[d]
            nc = tc + dc[d]
            if maze[nr][nc] == 3:
                return 1
            if not visited[nr][nc] and maze[nr][nc] != 1:
                visited[nr][nc] = 1
                q.append((nr, nc))
    return 0

for t in range(1, 11):
    tc = input()
    n = 16
    q = []
    visited = [[0] * n for _ in range(n)]
    maze = [list(map(int, input())) for _ in range(n)]
    ans = BFS(1, 1)
    print('#%d %d' % (t, ans))
