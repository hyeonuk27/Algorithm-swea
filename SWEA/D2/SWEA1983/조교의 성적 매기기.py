import sys
sys.stdin = open('input.txt')
import math

def get_total_score(m, f, h):
    total = m * 0.35 + f * 0.45 + h * 0.2
    return total

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    scores = []
    for i in range(n):
        mid, fin, hws = map(int, input().split())
        scores += [get_total_score(mid, fin, hws)]
        if i == k - 1:
            k_score = get_total_score(mid, fin, hws)

    my_scores = sorted(scores)[::-1]
    k_idx = my_scores.index(k_score) + 1
    p = math.ceil( k_idx / n * 10) - 1
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    ans = grade[p]
    print('#%d %s' % (t, ans))