import sys
sys.stdin = open('input.txt')


def B_to_D(B):
    D = 0
    for b in B:
        D = D * 2 + int(b)
    for i in range(len(B)):
        BtoD.append(D ^ (1 << i))


def check_T_in_D(T):
    for i in range(len(T)):
        num1 = num2 = 0
        for j in range(len(T)):
            if i != j:
                num1 = num1 * 3 + int(T[j])
                num2 = num2 * 3 + int(T[j])
            else:
                num1 = num1 * 3 + (int(T[j]) + 1) % 3
                num2 = num2 * 3 + (int(T[j]) + 2) % 3
        if num1 in BtoD:
            return num1
        if num2 in BtoD:
            return num2


for t in range(1, int(input())+1):
    B = input()
    T = input()
    BtoD = []
    B_to_D(B)
    ans = check_T_in_D(T)
    print('#%d %s' % (t, ans))