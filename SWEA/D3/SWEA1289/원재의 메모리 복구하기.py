import sys
sys.stdin = open('input.txt')

for t in range(1, 1 + int(input())):
    memory = input()
    n = len(memory)
    cnt = 0

    if memory[0] == '1':
        cnt += 1
    for i in range(1, n):
        cnt += 1 if memory[i-1] != memory[i] else 0

    print('#%d %d' % (t, cnt))