import sys
sys.setrecursionlimit(10**8)

def divide(ins,ine,prs,pre):
    if ins > ine or prs > pre:
        return
    rt = post_order[pre]
    pre_order.append(rt)
    l = pos[rt]-ins
    divide(ins,pos[rt]-1,prs,prs+l-1)
    divide(pos[rt]+1,ine,prs+l,pre-1)


n = int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))
pre_order = []
pos=[0]*(n+1)
for i in range(n):
    pos[in_order[i]] = i

divide(0,n-1,0,n-1)
for i in pre_order:
    print(i,end=" ")