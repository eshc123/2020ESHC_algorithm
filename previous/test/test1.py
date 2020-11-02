from itertools import product

m=['a','e','i','o','u']
a=[]
for j in range(1,6):
    for i in product(m,repeat = j):
        s=''
        for k in i:
            if k.isalnum():
                s+=k
        a.append(s)
a.sort()
print(a.index('i')+1)