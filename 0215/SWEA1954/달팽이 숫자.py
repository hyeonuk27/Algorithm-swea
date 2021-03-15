import sys
sys.stdin = open('input.txt')

# 델타 표 -  시계 방향
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for t in range(1, int(input())+1):
    n = int(input())
    space = [[0] * n for i in range(n)]

    num = 0 # space에 입력할 숫자
    nr, nc = 0, -1 # 초기 위치 -> 시작하자마자 이동하여 (0,0)에 1이 입력된다
    loop = n # 방향 전환 전까지 이동하는 칸 수
    d = 0 # 현재 방향 (델타표)

    for i in range(2*n-1):
        for j in range(loop):
            # 한 칸 이동
            nr += dr[d]
            nc += dc[d]
            # 입력할 숫자 1 증가
            num += 1
            # space에 num 입력
            space[nr][nc] = num

        # loop만큼 이동 후 방향 갱신
        d = (d + 1) % len(dr)
        # d가 홀수면 loop 1 감소
        if d % 2:
            loop -= 1

    print('#%d' % t)
    for i in space:
        print(*i)