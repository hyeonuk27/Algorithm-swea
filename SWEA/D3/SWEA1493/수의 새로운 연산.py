import sys
sys.stdin = open('input.txt')

def get_start(p):
    s = 1
    n = 1
    while s <= p:
        s += s
        n += 1
    return s-1, n-1

for t in range(1, int(input())+1):
    p, q = map(int, input().split())
    print(p,q)
    print(get_start(p))

