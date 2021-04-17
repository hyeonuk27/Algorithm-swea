import sys
sys.stdin = open('input.txt')

# 9 8 4 2 9 4 3 8 7 9 7 7 케이스 오류
# def chk_baby_gin():
#     for i in range(3, 7):
#         A = sorted(A_arr[:i])
#         B = sorted(B_arr[:i])
#         l = len(A)
#         for j in range(l-2):
#             if A[j] + 2 == A[j+1] + 1 == A[j+2] or A[j] == A[j+1] == A[j+2]:
#                 return 1
#             if B[j] + 2 == B[j+1] + 1 == B[j+2] or B[j] == B[j+1] == B[j+2]:
#                 return 2
#     return 0
#
# for t in range(1, int(input())+1):
#     cards = list(map(int, input().split()))
#     A_arr = cards[0:12:2]
#     B_arr = cards[1:12:2]
#     print('#%d %d' % (t, chk_baby_gin()))
