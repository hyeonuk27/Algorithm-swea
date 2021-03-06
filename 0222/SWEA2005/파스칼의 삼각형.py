import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = int(input())
    board = [[0] * n for _ in range(n)]

    # 0열과 n-1열에 1 채우기
    for i in range(n):
        for j in range(n):
            board[i][0] = 1
            if i == j:
                board[i][j] = 1

    # 1열 ~ n-2열까지 상 값 + 좌상 값 더해서 채우기
    for r in range(2, n):
        for c in range(1, n-1):
            board[r][c] = board[r-1][c] + board[r-1][c-1]

    # 숫자가 채워지지 않은 곳(0) 지우면서 출력하기
    print('#%d' % t)
    for i in range(n):
        for j in range(i+1):
            print(board[i][j], end=' ')
        print()