import sys
sys.stdin = open('input.txt')

def get_winner(a, b):
    if card[a] == 1 and card[b] == 2 or card[a] == 2 and card[b] == 3 or card[a] == 3 and card[b] == 1:
        return b
    else:
        return a

def get_group(s, e):
    if s == e:
        return s
    else:
        m = (s + e) // 2
        group1 = get_group(s, m)
        group2 = get_group(m + 1, e)
        return get_winner(group1, group2)

for t in range(1, int(input())+1):
    n = int(input())
    card = list(map(int, input().split()))
    ans = get_group(0, n - 1) + 1
    print('#%d %d' % (t, ans))

