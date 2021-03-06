import sys
sys.stdin = open('input.txt')

def check(puzzle):
    cnt = 0
    result = 0
    for i in range(n+2):
        for j in range(n+2):
            if puzzle[i][j]:
                cnt += 1
            else:
                if cnt == k:
                    result += 1
                cnt = 0
    return result

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    puzzle = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
    puzzle.insert(0, [0] * (n + 2))
    puzzle.append([0] * (n + 2))
    zip_puzzle = list(zip(*puzzle))
    ans = check(puzzle) + check(zip_puzzle)
    print('#%d %d' % (t, ans))