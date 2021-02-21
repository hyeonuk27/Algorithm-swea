import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())

if abs(A - B) == 2:
    if A > B:
        print('B')
    else:
        print('A')

else:
    if A > B:
        print('A')
    else:
        print('B')

