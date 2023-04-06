N=input().lower()
list_N=list(set(N))

list_cnt=[]

for i in list_N:
    cnt=N.count(i)
    list_cnt.append(cnt)

if list_cnt.count(max(list_cnt)) >= 2:
    print('?')

else:
    index_N=list_cnt.index(max(list_cnt))
    print(list_N[index_N].upper())