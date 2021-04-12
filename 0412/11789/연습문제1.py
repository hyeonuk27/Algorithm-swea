import sys
sys.stdin = open('input.txt')

def convert(num):
    D = 0
    for i in range(7):
        D += int(num[6-i]) * (2 ** i)
    tmp.append(D)

for t in range(1, int(input()) + 1):
    arr = input()
    tmp = []
    for i in range(0, len(arr), 7):
        num = arr[i:i+7]
        convert(num)
    ans = ' '.join(map(str, tmp))
    print('#%d %s' % (t, ans))