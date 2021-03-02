import sys
sys.stdin = open('input.txt')

def DFS(level):

    global min_sum
    arr_sum = 0
    for i in range(level):
        arr_sum += nums[i][arr[i]-1]
        if arr_sum > min_sum:
            return

    # 종료조건
    if level == n:
        min_sum = arr_sum
        return

    # DFS 확산
    for j in range(1, n+1):
        if visited[j]:
            continue
        visited[j] = 1
        arr[level] = j
        DFS(level + 1)
        visited[j] = 0

for t in range(1, int(input())+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * (n + 1)
    arr = [0] * n
    min_sum = 50
    DFS(0)
    print('#%d %d' % (t, min_sum))

