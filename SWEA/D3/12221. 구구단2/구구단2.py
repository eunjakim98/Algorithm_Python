TC=int(input())

for i in range(TC):
    A,B=map(int,input().split())
    ans=A*B
    if A>=10 or B>=10:
        ans=-1

    print('#%d %d'%(i+1,ans))