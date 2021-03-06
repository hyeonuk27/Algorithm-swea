import sys
sys.stdin = open('input.txt')

def paper(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    return paper(n - 1) + 2 * paper(n - 2)

for t in range(1, int(input())+1):
    N = int(input()) // 10
    result = paper(N)
    print('#%d %d' % (t, result))