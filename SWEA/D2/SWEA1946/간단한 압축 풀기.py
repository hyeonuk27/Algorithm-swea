import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = int(input())
    ans = ''
    for _ in range(n):
        char, num = input().split()
        ans += char * int(num)

    print('#%d' % t)
    for i in range(0, len(ans), 10):
        print(ans[i:i+10])