import sys
sys.stdin = open('input.txt')

for i in range(10):
    t = int(input())
    board = [input() for _ in range(100)]
    n = len(board)

    ans = 0
    for i in range(n):
        for s in range(n): # 시작 위치
            for e in range(n-1, s, -1): # 긴 것부터 검사, 마지막 위치
                Len = e - s + 1 # 길이

                # 가로
                if ans >= Len:
                    break
                for j in range(Len // 2):
                    if board[i][s + j] != board[i][e - j]:
                        break
                else:
                    ans = Len

                # 세로
                if ans >= Len:
                    break
                for j in range(Len // 2):
                    if board[s + j][i] != board[e - j][i]:
                        break
                else:
                    ans = Len

    print('#{} {}'.format(t, ans))