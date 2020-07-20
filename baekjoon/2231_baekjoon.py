N=int(input())
_min=N
for i in range(N+1):
    i=str(i)
    _list=[int(i)]
    for j in range(len(i)):
        _list.append(int(i[j]))
    if sum(_list)==N:
        if int(i)<_min:
            _min=int(i)
if _min==N:
    print(0)
else:
    print(_min)
