import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    n = int(input())
    password = input().split()
    m = int(input())
    orders = input().split()

    while orders:
        order = orders.pop(0)
        x = int(orders.pop(0))
        y = int(orders.pop(0))
        # 삽입 명령문 수행
        if order == 'I':
            for i in range(y):
                s = orders.pop(0)
                password.insert(x+i, s)
        # 삭제 명령문 수행
        else:
            for _ in range(y):
                password.pop(x)

    print('#%d %s' % (t, ' '.join(password[:10])))