import sys
sys.stdin = open('input.txt')

def calculator(cal_input):
    result = 0
    for i in cal_input:
        if i.isdigit() or not stack:
            stack.append(i)
        elif i != '.':
            if len(stack) < 2:
                return 'error'
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '+':
                    result = b + a
                elif i == '-':
                    result = b - a
                elif i == '*':
                    result = b * a
                elif i == '/':
                    result = b / a
                stack.append(result)
        elif i =='.':
            if len(stack) != 1:
                return 'error'
            else:
                return stack[-1]

for t in range(1, int(input())+1):
    cal_input = list(input().split())
    stack = []
    print('#%d %s' % (t, calculator(cal_input)))
