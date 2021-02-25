# 순열 재귀

arr = [1, 2, 3]

N = 3

sel = [0] * N # 결과들이 저장될 리스트
check = [0] * N # 해당 원소를 이미 사용했는지 안했는지에 대한 체크

def perm(idx):
    # 만약에 다 뽑아서 정리했다면
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            # 아직 사용하지 않았다면
            if check[i] == 0:
                # 값을 써라
                sel[idx] = arr[i]
                # 사용을 했다는 표시
                check[i] = 1
                # idx+1 호출
                perm(idx+1)
                # 다음 반복문을 위한 원상복구
                check[i] = 0

perm(0)