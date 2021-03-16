import sys
sys.stdin = open('input.txt')

def get_palindrome(board, n):
    global m
    cnt = 0
    for i in range(m):
        for j in range(m-n+1):
            temp = board[i][j:j+n]
            if temp == temp[::-1]:
                cnt += 1
    return cnt


for t in range(1, 11):
    n = int(input())
    m = 8
    board = [input() for _ in range(m)]
    board2 = list(zip(*board))

    row_cnt = get_palindrome(board, n)
    col_cnt = get_palindrome(board2, n)
    ans = row_cnt + col_cnt

    print('#%d %d' % (t, ans))
