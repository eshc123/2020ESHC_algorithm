##53% 에서 틀리거나 시간초과

import sys

xyz = list(map(int,sys.stdin.readline().split()))
a,b,c = xyz[:3],xyz[3:6],xyz[6:]
m = [(a[0]+b[0])/2,(a[1]+b[1])/2,(a[2]+b[2])/2]
al = (((a[0]-c[0])**2)+((a[1]-c[1])**2)+((a[2]-c[2])**2))**0.5
bl = (((b[0]-c[0])**2)+((b[1]-c[1])**2)+((b[2]-c[2])**2))**0.5
if a==b:
    print(format(0,".10f"))
    sys.exit()
l,r = a, b
i=1
while True:
    m = [(l[0] + r[0]) / 2, (l[1] + r[1]) / 2, (l[2] + r[2]) / 2]
    length = (((m[0] - c[0]) ** 2) + ((m[1] - c[1]) ** 2) + ((m[2] - c[2]) ** 2)) ** 0.5
    al = (((l[0] - c[0]) ** 2) + ((l[1] - c[1]) ** 2) + ((l[2] - c[2]) ** 2)) ** 0.5
    bl = (((r[0] - c[0]) ** 2) + ((r[1] - c[1]) ** 2) + ((r[2] - c[2]) ** 2)) ** 0.5
    if ((m[0]) == a[0] and m[1] == a[1] and (m[2]) == a[2]) or ((m[0]) == b[0] and (m[1]) == b[1] and (m[2]) == b[2]):
        print(format(length,".10f"))
        break
    if al < bl:
        r=m
    elif al > bl:
        l=m
    else :
        print(format(length,".10f"))
        break
