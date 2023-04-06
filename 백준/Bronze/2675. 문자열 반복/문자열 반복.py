T=int(input())

for i in range(T):
    S=input().split()
    text=''
    for j in S[1]:
        text += j*int(S[0])
    print(text)