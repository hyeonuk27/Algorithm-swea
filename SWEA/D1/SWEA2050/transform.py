import sys
sys.stdin = open('input.txt')

alphabet = list(input())

for i in alphabet:
    print(ord(i) - 64, end=' ')


