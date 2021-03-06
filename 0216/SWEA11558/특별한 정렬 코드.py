import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = int(input())
    num = list(map(int, input().split()))
    for i in range(10):
        for j in range(i+1, n):
            if i % 2:
                if num[i] > num[j]:
                    num[i], num[j] = num[j], num[i]
            else:
                if num[i] < num[j]:
                    num[i], num[j] = num[j], num[i]
    print("#%d %s" % (t, ' '.join(map(str, num[:10]))))