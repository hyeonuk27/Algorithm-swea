import sys
sys.stdin = open('input.txt')

# 시계방향, 8방향
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def game(c, r, friend):
    enemy = 2 if friend == 1 else 1
    board[r][c] = friend
    temp = []
    for d in range(8):
        nr = r + dr[d]
        nc = c + dc[d]
        while True:
            if board[nr][nc] == 0 or board[nr][nc] == 3 :
                temp = []
                break
            elif board[nr][nc] == friend:
                break
            elif board[nr][nc] == enemy:
                temp.append((nr, nc))
            nr += dr[d]
            nc += dc[d]
        for tr, tc in temp:
            board[tr][tc] = friend

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    board = [[3] + [0] * n + [3] for _ in range(n)]
    board.insert(0, [3] * (n + 2))
    board.append([3] * (n + 2))

    setup = n // 2
    board[setup][setup] = 2
    board[setup+1][setup+1] = 2
    board[setup][setup+1] = 1
    board[setup+1][setup] = 1

    for _ in range(m):
        r, c, friend = map(int, input().split())
        game(r, c, friend)

    B, W = 0, 0
    for i in range(n+2):
        B += board[i].count(1)
        W += board[i].count(2)
    print('#%d %d %d' % (t, B, W))