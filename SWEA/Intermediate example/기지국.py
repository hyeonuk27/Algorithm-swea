import sys
sys.stdin = open('input.txt')

def get_space(space):
    for r in range(n):
        for c in range(n):
            if space[r][c] !='X' and space[r][c] !='H':
                for k in range(1, ord(space[r][c]) - ord('A') + 2): #1
                    # 동쪽 check
                    if space[r][c+k] == 'H' and c + k < n:
                        space[r][c+k] = 'X'
                    # 서쪽 check
                    if space[r][c-k] == 'H' and 0 < c - k:
                        space[r][c-k] = 'X'
                    # 남쪽 check
                    if space[r+k][c] == 'H' and r + k < n:
                        space[r+k][c] = 'X'
                    # 북쪽 check
                    if space[r-k][c] == 'H' and 0 < r - k:
                        space[r-k][c] = 'X'
    return space

for t in range(1, int(input())+1):
    n = int(input())
    space = [list(input()) for _ in range(n)]

    ans = 0
    for r in range(n):
        for c in range(n):
            if get_space(space)[r][c] == 'H':
                ans += 1

    print('#%d %d' % (t, ans))
