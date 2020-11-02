import sys
lst= [int(input()) for _ in range(9)]
lst=sorted(lst)
s=sum(lst)
for i,j in enumerate(lst):
    for k in range(i+1,len(lst)):
        if s-j-lst[k]==100:
            for a,b in enumerate(lst):
                if a==i or a==k:
                    continue
                print(b)
            sys.exit(0)