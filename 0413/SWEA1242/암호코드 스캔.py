import sys
sys.stdin = open('input.txt', 'r')

decode = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
          '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}
print(len('05E35D9976EDD990'))
for t in range(1, int(input())+1):
    N, M = map(int, input().split())
