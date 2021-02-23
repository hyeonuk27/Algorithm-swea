import sys
sys.stdin = open('input.txt')

for t in range(1, int(input()) +1):
    txt = list(input())
    stack = []
    for i in txt:
        # stack이 비었거나, 문자가 stack의 top과 다를 때 push
        if len(stack) < 1 or stack[-1] != i:
            stack.append(i)
        # 문자가 stack의 top과 같을 때 pop
        else:
            stack.pop()

    ans = 0 if len(stack) < 1 else len(stack)
    print('#%d %d' % (t, ans))