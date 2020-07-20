R, B = map(int,input().split())


for i in range(1,int(B**(0.5))+1):
    if B%i ==0:
        if 2*i + (B//i)*2 + 4 == R:
            print(B//i+2, i+2)