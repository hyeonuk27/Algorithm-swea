import sys
sys.stdin = open('input.txt')

N = int(input())

ans = 0
for i in range(1, N+1):
    ans += i

print(ans)