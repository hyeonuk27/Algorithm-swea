import sys
sys.stdin = open('input.txt')

# push 함수
def push(v):
    if v == '{' or v == '(':
        stack.append(v)
        return
# pop 함수
def pop():
    if not len(stack):
        return -1
    return stack.pop(-1)

for tc in range(1, int(input())+1):
    t = input()
    stack = []
    ans = 1

    for i in t:
        push(i)
        if i == ')':
            pop1 = pop()
            if pop1 == ')':
                ans = 0
        elif i == '}':
            pop2 = pop()
            if pop2 == '}':
                ans = 0

    if stack:
        ans = 0
    print('#%d %d' % (tc, ans))








