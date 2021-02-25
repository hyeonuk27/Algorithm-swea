import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = 9
    board1 = [list(map(int, input().split())) for _ in range(n)]
    board2 = list(zip(*board1))
    ans = 1

    def chk_rowcol(arr):
        
    print('#%d %d' % (t, ans))