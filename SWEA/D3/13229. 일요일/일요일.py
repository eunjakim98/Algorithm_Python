day=[0,'MON','TUE','WED','THU','FRI','SAT','SUN']
T=int(input())

for i in range(T):
    S=input()
    if S=='SUN':
        print('#%d %d'%(i+1,7))
    else:
        print('#%d %d'%(i+1,7-day.index(S)))