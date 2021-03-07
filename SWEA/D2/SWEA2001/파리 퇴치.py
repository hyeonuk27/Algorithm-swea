import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1):
    N, M = map(int,input().split())

    # 2차원 배열 가져오기
    fly_arr = []
    for _ in range(N):
        in_arr = list(map(int, input().split()))
        fly_arr += [in_arr]

    max_kill = 0
    for i in range(N-M+1): # M-N+1개까지 열
        for j in range(N-M+1): # M-N+1개까지 행
            kill = 0
            for k in range(M): # M개까지 열
                for l in range(M): # M개까지 행
                    kill += fly_arr[i+k][j+l]
            if max_kill < kill:
                max_kill = kill

    print('#{} {}'.format(t, max_kill))