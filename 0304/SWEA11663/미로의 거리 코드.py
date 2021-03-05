import sys
sys.stdin = open('input.txt')

def get_start(N):
    for i in range(N + 2):
        for j in range(N + 2):
            if maze[i][j] == 3:
                return i, j

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(sr, sc):
    q = []
    visited = [[0] * (N + 2) for i in range(N + 2)]
    visited[sr][sc] = 0
    q.append((sr, sc))
    while q:
        tr, tc = q.pop(0)
        for d in range(4):
            nr = tr + dr[d]
            nc = tc + dc[d]
            if maze[nr][nc] == 2:
                return visited[tr][tc]
            if maze[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = visited[tr][tc] + 1
                q.append((nr, nc))
    return 0

for t in range(1, int(input()) + 1):
    N = int(input())
    maze = [[1] + list(map(int, input())) + [1] for _ in range(N)]
    maze.insert(0, [1] * (N + 2))
    maze.append([1] * (N + 2))
    sr, sc = get_start(N)
    ans = BFS(sr, sc)
    print('#%d %d' % (t, ans))