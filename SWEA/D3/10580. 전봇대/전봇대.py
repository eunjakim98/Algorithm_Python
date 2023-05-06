TC=int(input())

for i in range(TC):
    N = int(input())
    ind = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for j in range(N - 1):
        for k in range(j + 1, N):
            l1, r1 = ind[j]
            l2, r2 = ind[k]
            if ((l1 > l2 and r1 < r2) or (l1 < l2 and r1 > r2)):
                res+=1

    print(f'#{i+1} {res}')