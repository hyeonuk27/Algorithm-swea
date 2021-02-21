import sys
sys.stdin = open('SampleInput.txt')

N = int(input()) + 1

while N > 0:
    N -= 1
    print(N, end=' ')