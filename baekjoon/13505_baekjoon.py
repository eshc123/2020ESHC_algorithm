import sys

def str_xor():
    numbers = []
    for j in sorted(arr)[::-1]:
        if  2 ** index <= j:
            numbers.append(j)
        else:
            return numbers
    return numbers


N = int(sys.stdin.readline())
arr = set(map(int,sys.stdin.readline().split()))
index = len(bin(max(arr))) - 3
mxs = str_xor()
m = 0
for i in arr:
    for mx in mxs:
        if mx ^ i > m:
            m = mx ^ i
            if m==(2**index)-1:
                break
    if m == (2 ** index) - 1:
        break
print(m)

