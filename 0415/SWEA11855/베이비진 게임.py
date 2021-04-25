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
    B = [0] * 10
    for ai, bi in zip(cards[0::2], cards[1::2]):
        if chk_babygin(A, ai):
            return 1
        if chk_babygin(B, bi):
            return 2
    return 0

for t in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    ans = get_winner()
    print('#%d %d' % (t, ans))