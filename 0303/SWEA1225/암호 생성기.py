import sys
sys.stdin = open('input.txt')

def get_pw(data):
    idx = 1
    while data[-1] > 0:
        a = data.pop(0)
        data.append(a - idx % 6)
        idx += 1
        if idx % 6 == 0:
            idx = 1
    if data[-1] != 0:
        data[-1] = 0
    return data

for t in range(1, 11):
    tc = int(input())
    data = list(map(int, input().split()))
    print('#%d %s' % (tc, ' '.join(map(str, get_pw(data)))))