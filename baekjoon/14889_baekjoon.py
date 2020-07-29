def pmt(n,idx,a):
    if len(a)== n//2:
        print(a)
        return
    if idx >= n:
        return
    pmt(n,idx+1,a+[numbers[idx]])
    pmt(n, idx + 1, a )


N = int(input())
a = [list(map(int, input().split())) for i in range(N)]
numbers = [i for i in range(N)]
links = []
starts = []
pmt(N,0,[])

# for i in range(1,2**(N//2) ):
#     link=[]
#     start=[]
#     temp = (i << (N//2) ) | (2**(N//2)-1 - i)
#     print(bin(temp))
#     for j in range(N):
#         if ~temp & (1<<j) :
#             print(j,~temp & (1<<j))
#             link.append(j)
#         else:
#             start.append(j)
#     links.append(link)
#     starts.append(start)

print(links,starts)
