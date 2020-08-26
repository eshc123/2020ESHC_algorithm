x, y, c = map(float,input().split())

l,r = 1,min(x,y)
ans=(l+r)/2.0
while r-l> 0.000001:
    mid = (l+r)/2.0
    h1 = ((x**2)-(mid**2))**0.5
    h2 = ((y ** 2) - (mid ** 2)) ** 0.5
    if c>(h1*h2)/(h1+h2):
        ans=mid
        r=mid
    elif c<=(h1*h2)/(h1+h2):
        l=mid

print(ans)