import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    n = int(input())
    password = list(input().split())
    m = int(input())
    orders = input().split()

    while len(orders) > 0:
        I = orders.pop(0)
        idx = orders.pop(0)
        N = orders.pop(0)
        for i in range(int(N)):
            order = orders.pop(0)
            password.insert(int(idx)+i, order)
    print('#%d %s' % (t, ' '.join(password[:10])))

