import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    A, B = input().split()
    a, b = len(A), len(B)
    n = A.count(B)
    print('#%d %d' % (t, a - b * n + n))