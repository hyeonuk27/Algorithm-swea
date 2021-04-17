import sys
sys.stdin = open('input.txt')

def get_subset_sum():
    min_S = 987654321
    for i in range(1, 1 << N+1):
        S = 0
        for j in range(N):
            if i & (1 << j):
                S += heights[j]
        if B <= S < min_S :
            min_S = S
    return min_S - B


for t in range(1, int(input())+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    print('#%d %d' % (t, get_subset_sum()))

# 베스트 코드
# def f(i, s):
#     global minV
#     if minV < s or minV == B:
#         return
#     if s >= B:
#         minV = min(minV, s)
#         return
#     if i == N:
#         return
#     if s + rs[i] < B:
#         return
#     f(i + 1, s + H[i])
#     f(i + 1, s)
#
#
# for tc in range(1, 1 + int(input())):
#     N, B = map(int, input().split())
#     H = list(map(int, input().split()))
#     minV = 200001
#     rs = H.copy()
#     for i in range(N - 2, -1, -1):
#         rs[i] += rs[i + 1]
#
#     f(0, 0)
#     print('#{} {}'.format(tc, minV - B))