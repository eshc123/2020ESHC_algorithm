s = list(input())
l = len(s)
m='z'*l
for i in range(1,l):
    for j in range(i+1,l):
        a,b,c = s[:i],s[i:j],s[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        if ('').join(a+b+c) < m:
            m=('').join(a+b+c)
print(m)
