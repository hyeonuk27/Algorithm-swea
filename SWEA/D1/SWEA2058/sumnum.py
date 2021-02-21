import sys
sys.stdin = open('input.txt')

N = int(input())

sum_num = 0
while N > 0:
    sum_num += N % 10
    N = int(N / 10)

print(sum_num)

