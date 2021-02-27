import sys
sys.stdin = open('input.txt')

def get_palindrome(board, n, m):
    for i in range(n):
        # (case3) n, m이 다른 경우 n - m + 1
        for j in range(n - m + 1):
            word = board[i][j:j+m]
            # palindrome 판단하기
            if word == word[::-1]:
                return word

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board1 = [list(input()) for i in range(m)]
    # 전치 행렬 구하기
    board2 = list(zip(*board1))

    # 가로 검사 실패 시에만 세로 검사
    if get_palindrome(board1, n, m) == None:
        ans = get_palindrome(board2, n, m)
    else:
        ans = get_palindrome(board1, n, m)
    print('#%d %s' % (t, ''.join(ans)))