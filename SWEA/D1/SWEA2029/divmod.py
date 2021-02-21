import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    a, b = map(int, input().split())

    quotient = int(a / b)
    remainder = a % b

    print('#{} {} {}'.format(t, quotient, remainder))