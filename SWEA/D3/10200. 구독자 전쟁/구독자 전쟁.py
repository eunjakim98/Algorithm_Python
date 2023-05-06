T = int(input())

for i in range(T):
    N,A,B = map(int, input().split())

    if A+B > N:
        print(f'#{i+1} {min(A,B)} {A+B-N}')
    else:
        print(f'#{i+1} {min(A,B)} 0')