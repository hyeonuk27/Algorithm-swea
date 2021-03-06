import sys
sys.stdin = open('input.txt')

def rotate_90(space):
    space_90 = [[''] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            space_90[c][n-1-r] = space[r][c]
    return space_90

def mini(space):
    mini = 0
    for r in range(m):
        for c in range(m-r):
            mini += space[r][c]
    return mini

for t in range(1, int(input())+1):
    n =  int(input())
    m = n // 2
    space = [list(map(int, input())) for i in range(n)]

    total = 0
    for r in range(n):
        for c in range(n):
           total += space[r][c]

    space_90 = rotate_90(space)
    space_180 = rotate_90(space_90)
    space_270 = rotate_90(space_180)

    mini1 = mini(space)
    mini2 = mini(space_90)
    mini3 = mini(space_180)
    mini4 = mini(space_270)

    ans = total - mini1 - mini2 - mini3 - mini4
    print('#%d %d' % (t, ans))