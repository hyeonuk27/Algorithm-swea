import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    txt = input()

    for i in range(1, len(txt)):
        if txt[0:i] == txt[0+i:0+i+i]:
            ans = i
            break
    print('#%d %d' % (t, ans))
