def search(number):
    arr = set()
    for i in range(1,len(number)):
        for j in range(len(number)-i+1):
            t = int(number[j:j+i])
            if t!=0:
                arr.add(t)
    return list(arr)


n = int(input())
d = [False for _ in range(n+1)]
flag_num = -1
for i in range(10,n+1):
    flag = False

    for num in sorted(search(str(i))):
        if not d[i-num]:
            flag = True
            flag_num= num
            break
    if flag:
        d[i]=True
    else:
        flag_num = -1
print(flag_num)
