import sys
sys.stdin = open('input.txt', 'r')

pw = ['0001101', '0011001', '0010011', '0111101', '0100011',
      '0110001', '0101111', '0111011', '0110111', '0001011']
pattern = {key: value for key, value in zip(pw, range(len(pw)))}


# 1개 코드 반환 - tuple로 반환
def get_one_code(arr, cnt):
    nbits = cnt * 7 # 글자당 필요 비트 수
    n_length = nbits << 3 # 코드당 필요 비트 수
    temp = arr[-n_length:]
    code = []
    for i in range(0, len(temp), nbits):
        num = pattern.get(temp[i:i + nbits][::cnt], 'X') #[::cnt] 건너뛰면서 8자리 출력
        if num == 'X':
            return 0  # 실패
        code.append(num)
    return tuple(code)


def get_code_by_line(arr):
    c_list = set()
    while arr:
        cnt = 1
        while True: # 적합한 코드가 만들어 질때까지 -> 적합한 코드 : 8개 숫자를 가진 tuple
            arr = arr.zfill(cnt * 56)
            code = get_one_code(arr, cnt)  # 배열과 끝위치 전달
            if code != 0: # 적합한 코드를 만들면
                c_list.add(code)
                n_bits = (cnt * 7) << 3  # *8  코드를 만들 때 사용한 bit 수
                arr = arr[:len(arr) - n_bits].rstrip('0')
                break
            cnt += 1 # 적합한 코드를 만들지 못하면
    return c_list


def get_codes(arr):
    code_list = set()
    for x in arr:
        if len(x) == 0: continue
        y = bin(int(x, 16))[2:].rstrip('0')
        codes = get_code_by_line(y)
        code_list = code_list.union(codes)
    return code_list


def check_info(arr):
    code = sum(arr[:-1:2]) * 3 + sum(arr[1::2])
    return sum(arr) if not code % 10 else 0


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    data = set()
    for _ in range(N):
        data.add(input()[:M].rstrip('0'))
    sol = sum(check_info(code) for code in get_codes(data))
    print('#%d %d' % (t, sol))