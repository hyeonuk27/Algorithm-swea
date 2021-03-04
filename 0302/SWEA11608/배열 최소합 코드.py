import sys
sys.stdin = open('input.txt')

# 특정 행(level)에서 사용할 열을 선택함
# level : 행 번호
# s : 선택된 열에 있는 값의 합

def DFS_sum(level, s):
    global min_sum
    # 가지치기
    if min_sum <= s:
        return
    # 종료조건
    if level >= n:
        if min_sum > s:
            min_sum = s
        return
    # DFS 호출 - 열 번호 선택
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            DFS_sum(level + 1, s + data[level][i])
            visited[i] = 0


for t in range(1, int(input())+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    min_sum = float('inf')
    DFS_sum(0, 0)
    print('#%d %d' % (t, min_sum))