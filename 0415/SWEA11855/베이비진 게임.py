import sys
sys.stdin = open('input.txt')

def chk_babygin(P, pi):
    P[pi] += 1
    if P[pi] == 3:
        return 1
    for i in range(8):
        if P[i] >= 1 and P[i+1] >=1 and P[i+2] >= 1:
            return 1
    return 0


def get_winner():
    A = [0] * 10
    B = [0] * 10  # index error
    for ai, bi in zip(cards[0::2], cards[1::2]): # 자료 묶기
        if chk_babygin(A, ai): # 함수 연결
            return 1
        if chk_babygin(B, bi):
            return 2
    return 0

for t in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    ans = get_winner()
    print('#%d %d' % (t, ans))


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
