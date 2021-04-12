import sys
sys.stdin = open('input.txt')

lookup = {'001101': '0',
          '010011': '1',
          '111011': '2',
          '110001': '3',
          '100011': '4',
          '110111': '5',
          '001011': '6',
          '111101': '7',
          '011001': '8',
          '101111': '9'
}

def get_end_point(b):
    i = len(b)-1
    while b[i] == '0':
        i -= 1
    return i

for t in range(1, int(input())+1):
    b = ''
    for s in input():
        b += bin(int(s, 16))[2:].zfill(4)
    code = []
    ei = get_end_point(b)
    for i in range(len(b)-ei-1, ei+1, 6):
        code.append(lookup[b[i:i+6]])
    print('#%d %s' % (t, ', '.join(code)))