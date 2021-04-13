import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    _, hexa = input().split()
    print('#%d %s' % (t, bin(int(hexa, 16))[2:].zfill(len(hexa)*4)))