T=int(input())

for i in range(T):
    S=input()
    cnt=0
    for j in S:
        if j=='x':
            cnt+=1
    if cnt<=7:
        print('#%d %s'%(i+1,'YES'))
    else:
        print('#%d %s'%(i+1,'NO'))