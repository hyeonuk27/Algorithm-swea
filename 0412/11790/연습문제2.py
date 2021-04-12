import sys
sys.stdin = open('input.txt')

def convert(N):
    d = 0
    for j in range(len(N)):
        d += int(N[len(N)-j-1]) * (2 ** j)
    D.append(d)

for t in range(1, int(input())+1):
    b = ''
    for s in input():
        b += format(int(s, 16), 'b').zfill(4)
    D = []
    for i in range(0, len(b), 7):
        B = b[i:i+7]
        convert(B)
    ans = ', '.join(map(str, D))
    print('#%d %s' % (t, ans))