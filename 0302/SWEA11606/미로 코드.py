import sys
sys.stdin = open('input.txt')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 출발점
def get_start_point(maze, n):
    for i in range(n+2):
        for j in range(n+2):
            if maze[i][j] == 2:
                return i, j
    return 'error'

# DFS
def find_route(r, c):
    # 방문 표시
    visit[r][c] = 1
    # 종료조건
    if maze[r][c] == 3:
        global ans
        ans = 1
        return

    # DFS 호출
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if maze[nr][nc] != 1 and visit[nr][nc] == 0:
            find_route(nr, nc)

for t in range(1, int(input())+1):
    n = int(input())
    maze = [[1] + list(map(int, input())) + [1] for _ in range(n)]
    maze.insert(0, [1] * (n + 2))
    maze.append([1] * (n + 2))
    visit = [[0]*(n+2) for _ in range(n+2)] ##
    sr, sc = get_start_point(maze, n)
    ans = 0
    find_route(sr, sc)
    print('#%d %d' % (t, ans))