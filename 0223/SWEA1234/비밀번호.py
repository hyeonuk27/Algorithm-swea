import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    n, pw = input().split()
    # .append()와 .pop() 사용하기 위해 리스트로 형변환
    pw = list(pw)

    stack = []
    for i in pw:
        if len(stack) < 1 or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()

    print('#%d %s' % (t, ''.join(stack)))