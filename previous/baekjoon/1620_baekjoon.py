N, M = map(int,input().split())
pockemons = dict()
for i in range(N):
    pockemons[input()]=i+1
for i in range(M):
    m = input()
    if m in pockemons.keys():
        print(pockemons[m])
