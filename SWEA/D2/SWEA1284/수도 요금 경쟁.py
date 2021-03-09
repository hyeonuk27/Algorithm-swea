import sys
sys.stdin = open('input.txt')

def get_charge_A(P, W):
    charge = P * W
    return charge

def get_charge_B(Q, R, W):
    base_charge = Q
    if W <= R:
        charge = base_charge
    else:
        charge = base_charge + (W - R) * S
    return charge

for t in range(1, int(input())+1):
    P, Q, R, S, W = map(int, input().split())
    A = get_charge_A(P, W)
    B = get_charge_B(Q, R, W)
    ans = B if A > B else A
    print('#%d %d' % (t, ans))