import sys
sys.stdin = open('input.txt')

# 출발점(좌상 좌표), sub_matrix 개수 찾기
def get_start_point():
    start_point = []
    for r in range(n):
        for c in range(n):
            if matrix[r][c] != 0 and matrix[r-1][c] == 0 and matrix[r][c-1] == 0:
                start_point.append((r, c))
    return start_point, len(start_point) # 출발점, sub_matrix 개수

# 도착점(우하 좌표) 찾기
def get_end_point(sr, sc): # 0,0 / 2,0
    er, ec = sr, sc
    while matrix[er][ec+1] != 0:
        ec += 1
    while matrix[er+1][ec] != 0:
        er += 1
    return er, ec

for t in range(1, int(input())+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # 출발점, 도착점 이용해 행렬 찾기
    start_points, N = get_start_point()
    sub_matrix = []
    for sr, sc in start_points:
        er, ec = get_end_point(sr, sc)
        sub_matrix += [(er-sr+1, ec-sc+1)]

    # 행렬 정렬하기
    sub_matrix.sort(key=lambda x: (x[0] * x[1], x[0]))

    print('#%d %d' % (t, N), end =' ')
    for i, j in sub_matrix:
        print(i, j, end=' ')
    print()