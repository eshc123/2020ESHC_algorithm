N = int(input())
s=0
l = len(str(N))-1
for i in range(0, l):
    s += 9*(10**i)*(i+1)
s+=(N-(10**l)+1)*(l+1)
print(s)

'''
1~9 : 9개 * 1 // 
10~99 : 90개 * 2 // (9
100~999 : 900개 * 3
...
'''