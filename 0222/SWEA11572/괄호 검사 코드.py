import sys
sys.stdin = open('input.txt')

# push 함수
def push(t):
    if t == '{' or t == '(':
        stack.append(t)
        return
# pop 함수
def pop():
    if not len(stack):
        return -1
    return stack.pop(-1)

for tc in range(1, int(input())+1):
    text = input()
    stack = []
    ans = 0
    for t in text:
        push(t)
        # 오른쪽 괄호를 만난 경우 pop하여 정상 / 오류 검사
        if t == ')':
            pop1 = pop()
            # 정상 괄호
            if pop1 == '(':
                ans = 1
            # 오류 괄호 (pop과 다르거나 빈 경우)
            else:
                ans = 0

        # 오른쪽 괄호를 만난 경우 pop하여 정상 / 오류 검사
        elif t == '}':
            pop2 = pop()
            # 정상 괄호
            if pop2 == '{':
                ans = 1
            # 오류 괄호 (pop과 다르거나 빈 경우)
            else:
                ans = 0

    # 마지막까지 조사 이후 남아있으면 오류
    if stack:
        ans = 0
    print('#%d %d' % (tc, ans))








