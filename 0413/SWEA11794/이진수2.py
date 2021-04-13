import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N = float(input())
    res =''
    for i in range(1, 14):
        check = N - 2 ** (-i)
        if check > 0:
            res += '1'
            N = check
        elif check < 0:
            res += '0'
        else:
            res += '1'
            break
    ans = 'overflow' if i == 13 else res
    print('#%d %s' % (t, ans))

