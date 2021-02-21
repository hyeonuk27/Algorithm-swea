import sys
sys.stdin = open('input.txt')

# 절대값 반환 함수
def get_abs(num):
    if num > 0:
        return num
    else:
        return -num

# 델타 표 - fix
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
m = len(dr) #4

for t in range(1, int(input())+1):
    space = [list(map(int, input().split())) for _ in range(5)]
    n = len(space) #5
    # 이중 for문으로 전체 행렬 돌기
    ans = 0
    for r in range(n):
        for c in range(n):
            # for 문으로 델타 표 참조해 이웃 요소 좌표 구하기
            for d in range(m):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < n:
                    ans += get_abs(space[r][c] - space[nr][nc])
    print('#%d %d' % (t, ans))