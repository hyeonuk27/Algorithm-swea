import sys
sys.stdin = open('input.txt')

# 우선순위 참조표
icp = {')': -1, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
isp = {')': -1, '*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

def get_postfix(cal_input):
    result = []
    for i in cal_input:
        # .isdigit() 숫자인지 확인하는 함수, 문자열이더라도 숫자가 저장된 경우 true
        if i.isdigit():
            result.append(i)
        # ')'는 '('를 만나기 전까지 pop해서 출력
        elif i == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            # '('를 만나면 pop만 함
            stack.pop()
        else:
            # 빈 스택이면 push
            if not stack:
                stack.append(i)
            # i가 top 연산자보다 우선순위가 높으면 push
            elif icp[i] > isp[stack[-1]]:
                stack.append(i)
            # i가 top보다 우선순위가 낮으면
            # top이 i보다 우선순위가 낮을 때까지 pop해서 출력
            else:
                while stack and icp[i] <= isp[stack[-1]]:
                    a = stack.pop()
                    result.append(a)
                # 빈 스택이면 push
                stack.append(i)
    # 스택에 남은 것 pop해서 출력
    while stack:
        a = stack.pop()
        result.append(a)
    return result

# step 2
def get_calculation(postfix):
    for i in postfix:
        # .isdigit() 숫자인지 확인하는 함수, 문자열이더라도 숫자가 저장된 경우 true
        if i.isdigit():
            stack.append(i)
        else:
            # - 와 / 는 연산 순서가 중요하다
            second = int(stack.pop())
            first = int(stack.pop())
            if i == '+':
                result = first + second
                stack.append(result)
            elif i == '-':
                result = first - second
                stack.append(result)
            elif i == '*':
                result = first * second
                stack.append(result)
            elif i == '/':
                result = first / second
                stack.append(result)
    return(stack[-1])


for t in range(1, 11):
    n =  int(input())
    cal_input = input()
    stack = []
    postfix = get_postfix(cal_input)
    ans = get_calculation(postfix)
    print('#%d %d' % (t, ans))

