import sys
sys.stdin = open('input.txt')

card = {'S' : 0, 'D' : 1, 'H' : 2, 'C' : 3}

for t in range(1, int(input())+1):
    x = input()
    card = [x[i:i+3] for i in range(0, len(x), 3)] ##
    cnt = [[0] * (13 + 1) for _ in range(4)]


    for i in card:
        for j in range(1, 3):
            if i == card[j]:
                print('fdfd')
                break

    for j in card:
        r = shape[j[0]]
        c = int(j[1:3])
        cnt[r][c] += 1

    # for k in cnt:
    #     for l in k:
    #         if l == 2:
    #             print('error')
    #             break
    #         break
    #
    #
    #
    ans = []
    for k in cnt:
        temp = 0
        for l in k:
            if l < 2 :
                temp += l
            else:
                print(dfd)
                break
        ans += [13 - temp]
    print(ans)
