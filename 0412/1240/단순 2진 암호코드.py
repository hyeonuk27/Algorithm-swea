import sys
sys.stdin = open('input.txt')

decode = {'0001101': '0',
          '0011001': '1',
          '0010011': '2',
          '0111101': '3',
          '0100011': '4',
          '0110001': '5',
          '0101111': '6',
          '0111011': '7',
          '0110111': '8',
          '0001011': '9'
}

def is_right_code(code):
    odd = even = 0
    for i in range(8):
        if i % 2:
            even += int(code[i])
        else:
            odd += int(code[i])
    if (odd * 3 + even) % 10:
        return 0
    return odd + even

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    tmp = set()
    for _ in range(N):
        num = input().strip('0')
        if num:
            tmp.add(num.zfill(56))
    code =''
    for i in range(0, 56, 7):
        key = list(tmp)[0][i:i+7]
        code += decode[key]
    ans = is_right_code(code)
    print('#%d %d' % (t, ans))
