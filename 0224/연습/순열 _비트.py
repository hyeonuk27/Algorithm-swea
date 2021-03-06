# 순열 재귀 - 비트

arr = [1, 2, 3]
N = 3
sel = [0] * N # 뽑은 결과를 적음
check = [0] * N # 해당 원소를 이미 사용했는지 안했는지에 대한 체크

# check 10진수 정수
def perm(idx, check):
    # 만약에 다 뽑아서 정리했다면
    if idx == N:
        print(sel)
        return

    for j in range(N):
        # j번째 원소를 활용을 했군, 그럼 쓰면 안되지.
        if check & (1 << j): continue

        # 값을 써라
        sel[idx] = arr[j]
        # 전달 인자로 던지는 순간 일회성만 사용하고 끝이 나므로, 원상복구가 필요없다
        perm(idx+1, check | (1<<j))

perm(0, 0)