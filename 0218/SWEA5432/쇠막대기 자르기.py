import sys
sys.stdin = open('input.txt')

def get_cnt(n):
    layer = cnt = 0
    for i in range(n):
        if data[i] == ')' and data[i-1] != '(':
            layer -= 1
            cnt += 1
        elif data[i] == '(' and data[i+1] !=')':
            layer += 1
        elif data[i] == '(' and data[i+1] ==')':
            cnt += layer
    return cnt

for t in range(1, int(input())+1):
    data = input()
    n = len(data)
    print('#%d %d' % (t, get_cnt(n)))