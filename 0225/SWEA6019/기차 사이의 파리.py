import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    d, a, b, f = map(int, input().split())
    d_fly = f * d / (a + b)
    print('#%d %.10f' % (tc, d_fly))