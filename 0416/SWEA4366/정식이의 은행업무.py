import sys
sys.stdin = open('input.txt')


def f(b, t):
    b_int = 0
    for x in b:
        b_int = b_int * 2 + int(x)
    binary = []
    for i in range(len(b)):
        binary.append(b_int ^ (1 << i))

    for i in range(len(t)):
        num1 = 0
        num2 = 0
        for j in range(len(t)):
            if i != j:
                num1 = num1 * 3 + int(t[j])
                num2 = num2 * 3 + int(t[j])
            else:
                num1 = num1 * 3 + (int(t[j]) + 1) % 3  # 0->1 1->2 2->0
                num2 = num2 * 3 + (int(t[j]) + 2) % 3  # 0->2 1-> 0 2->1
        if num1 in binary:
            return num1
        if num2 in binary:
            return num2


T = int(input())

for tc in range(1, T + 1):
    b = input()
    t = input()

    r = f(b, t)
    print('#%d %s' % (tc, r))