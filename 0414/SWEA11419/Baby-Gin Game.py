import sys
sys.stdin = open('input.txt')

def check_baby_gin(c):
    flag = 0
    for i in range(0, 4, 3):
        if int(c[i]) + 2 == int(c[i+1]) + 1 == int(c[i+2]):
            flag += 1
        if c[i] == c[i+1] == c[i+2]:
            flag += 1
    return flag

def perm(n, k):
    if k == n:
        comb.add(''.join(num))
    for i in range(k, n):
        num[k], num[i] = num[i], num[k]
        perm(n, k + 1)
        num[k], num[i] = num[i], num[k]

for t in range(1, int(input())+1):
    num = list(input()[:6])
    comb = set()
    perm(6, 0)
    for c in comb:
        if check_baby_gin(c) == 2:
            ans = 'Baby Gin'
            break
    else:
        ans = 'Lose'
    print('#%d %s' % (t, ans))