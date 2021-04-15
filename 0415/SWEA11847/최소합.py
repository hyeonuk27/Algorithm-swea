import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = int(input())
    grid = [[0] + list(map(int, input().split())) for _ in range(n)]
    grid.insert(0, [0] * (n+1))
    for i in range(1, n+1):
        for j in range(1, n+1):
            if grid[i][j-1] and grid[i-1][j]:
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])
            else:
                grid[i][j] += grid[i][j-1] + grid[i-1][j]
    print('#%d %d' % (t, grid[n][n]))