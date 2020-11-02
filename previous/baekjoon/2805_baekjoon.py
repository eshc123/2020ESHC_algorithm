import sys

N, M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
l, r = 0, max(trees)

while True:
    if l>r:
        break
    mid = (l+r)//2
    total = 0
    for tree in trees:
        if mid<tree:
            total+=tree-mid
    if total< M:
        r=mid-1
    else:
        l=mid+1
print(r)