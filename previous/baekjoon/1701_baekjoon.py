cubelang = input()
mx = 0
for idx in range(len(cubelang)):
    pi= [0 for __ in range(len(cubelang))]
    p = cubelang[idx:]
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    mx = max(mx,max(pi))
print(mx)