import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1):
    N, M = map(int,input().split())

    fly_arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for i in range(N-M+1): # M-N+1개까지 열 / 좌상단 좌표
       for j in range(N-M+1): # M-N+1개까지 행 / 좌상단 좌표
            kill = 0
            for k in range(M): # M개까지 열
                for l in range(M): # M개까지 행
                    kill += fly_arr[i+k][j+l]
            if max_kill < kill:
                max_kill = kill

    print('#{} {}'.format(t, max_kill))



