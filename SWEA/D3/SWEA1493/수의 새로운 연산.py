import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    p, q = map(int, input().split())
    print(p,q)
    print(get_start(p))

