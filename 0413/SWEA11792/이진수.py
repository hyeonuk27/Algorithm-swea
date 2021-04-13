import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, Hexa = input().split()
    ans = ''
    for H in Hexa:
        ans += bin(int(H, 16))[2:].zfill(4)
    print('#%d %s' % (t, ans))