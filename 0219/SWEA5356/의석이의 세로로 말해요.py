import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    chars = [list(input()) for _ in range(5)]

    max_len = 0
    for char in chars:
        if max_len < len(char):
            max_len = len(char)

    for char in chars:
        while len(char) < max_len:
            char.append('')

    new_chars = list(zip(*chars))
    ans = ''
    for i in new_chars:
        ans += ''.join(i)
    print('#%d %s' % (t, ans))