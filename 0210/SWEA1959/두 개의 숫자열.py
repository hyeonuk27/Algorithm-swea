import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_num = float('-inf')

    if N < M :
        for i in range(M-N+1):
            result = 0
            for j in range(N):
                result += A[j] * B[i+j]
            if max_num < result:
                max_num = result
    else:
        for i in range(N-M+1):
            result = 0
            for j in range(M):
                result += B[j] * A[i+j]
            if max_num < result:
                max_num = result

    print('#{} {}'.format(t, max_num))