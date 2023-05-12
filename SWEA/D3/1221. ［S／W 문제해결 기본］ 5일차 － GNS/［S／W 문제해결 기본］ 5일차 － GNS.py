num_str=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T=int(input())

for _ in range(T):
    tc,N=map(str,input().split())
    N=int(N)
    S=list(input().split())
    num_int=[]
    num_sort=[]
    for i in S:
        num_int.append(num_str.index(i))
    num_int.sort()
    for i in num_int:
        num_sort.append(num_str[i])
    print(tc)
    print(*num_sort)