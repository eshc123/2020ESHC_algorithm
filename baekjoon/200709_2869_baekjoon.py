import sys
a,b,c = sys.stdin.readline().split()
A,B,V = int(a),int(b),int(c)
if (V-B)%(A-B)==0:
    print((V-B)//(A-B))
else :
    print((V-B)//(A-B)+1)
