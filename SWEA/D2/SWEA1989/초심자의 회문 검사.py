import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    word = input()
    if word == word[::-1]:
        ans = 1
    else:
        ans = 0
    print('#%d %d' % (t, ans))