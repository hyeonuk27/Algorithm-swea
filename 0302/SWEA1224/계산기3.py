import sys
sys.stdin = open('input.txt')

isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

def get_postfix(cal_input):
    postfix = ''
    for i in cal_input:
        if i.isdigit():
            postfix += i
        elif i == ')':
            while stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            if not stack or icp.get(i) > isp.get(stack[-1]):
                stack.append(i)
            else:
                while stack and icp.get(i) <= isp.get(stack[-1]):
                    postfix += stack.pop()
                stack.append(i)
    while stack:
        postfix += stack.pop()
    return postfix

operater = {'+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
}

def calculation(postfix):
    for i in postfix:
        if i.isdigit():
            stack.append(int(i))
        else:
            b, a = stack.pop(), stack.pop()
            stack.append(operater[i](a, b))
    return stack[-1]

for t in range(10):
    n = int(input())
    cal_input = input()
    stack = []
    postfix = get_postfix(cal_input)
    ans = calculation(postfix)
    print('#%d %d' % (t+1, ans))

