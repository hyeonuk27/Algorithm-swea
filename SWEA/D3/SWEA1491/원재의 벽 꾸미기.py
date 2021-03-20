import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N, A, B = map(int, input().split())
    Min = float('inf')
    for i in range(1, int(N**0.5)+1):
        # N - R * C 가 최소값인 경우
        R, C = i, N // i
        Min = min(Min, A * abs(R - C) + B * (N - R * C))
    # R - C 가 최소값인 경우
    R = C = int(N**0.5)
    Min = min(Min, A * abs(R - C) + B * (N - R * C))
    print('#%d %d' % (t, Min))