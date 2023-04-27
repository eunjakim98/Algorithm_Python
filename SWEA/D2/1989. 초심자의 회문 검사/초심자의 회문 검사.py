T=int(input())

for i in range(T):
    word=input()
    a=word[::-1]
    if word==a:
        print('#%d %d'%(i+1,1))
    else:
        print('#%d %d'%(i+1,0))