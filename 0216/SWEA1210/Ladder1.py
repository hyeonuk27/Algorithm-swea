import sys
sys.stdin = open('input.txt')

# 델타표 좌 우
dr = [0, 0]
dc = [-1, 1]

for t in range(1, 11):
    tc = int(input())
    space = [list(map(int, input().split())) for _ in range(100)]
    n = 100

    # 마지막 행에서 2를 찾아서 출발 위치 찾기
    for i in range(n):
        if space[99][i] == 2:
            sc = i
            break

    # 출발점 초기화
    sr, sc = n - 1, sc

    # 첫 번째 행에 도착하면 반복문 종료
    while sr > 0:

        # 왼쪽으로 방향 전환
        if sc > 0 and space[sr][sc-1] == 1:
            while sc > 0 and space[sr][sc-1] != 0:
                sr += dr[0]
                sc += dc[0]
            sr -= 1

        # 오른쪽으로 방향 전환
        elif sc < n - 1 and space[sr][sc+1] == 1:
            while sc < n - 1 and space[sr][sc+1] != 0:
                sr += dr[1]
                sc += dc[1]
            sr -= 1

        # 방향 전환이 아니라면 위로 올라가기
        else:
            sr -= 1
    print('#%d %d' % (tc, sc))