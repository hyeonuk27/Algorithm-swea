import sys
sys.stdin = open('input.txt')

# tc가 10,000개라 print문을 for문에 넣으면 실행시간이 길어진다
# 모아서 출력하자
ans = []
for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    res = 'ON' if bin(M)[2:][-N:] == '1'* N else 'OFF'
    ans.append('#%s %s' % (t, res))
print('\n'.join(ans))