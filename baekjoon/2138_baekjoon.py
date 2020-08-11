def change(i):
    if bulbs[0][i]=='0':
        bulbs[0][i]='1'
    else: bulbs[0][i]='0'
    if bulbs[0][i-1]=='0':
        bulbs[0][i-1]='1'
    else: bulbs[0][i-1]='0'
    if bulbs[0][i+1]=='0':
        bulbs[0][i+1]='1'
    else: bulbs[0][i+1]='0'
    return

def change1(i):
    if bulbs[0][i]=='0':
        bulbs[0][i]='1'
    else: bulbs[0][i]='0'
    if bulbs[0][i+1]=='0':
        bulbs[0][i+1]='1'
    else: bulbs[0][i+1]='0'
    return

def change2(i):
    if bulbs[0][i]=='0':
        bulbs[0][i]='1'
    else: bulbs[0][i]='0'
    if bulbs[0][i-1]=='0':
        bulbs[0][i-1]='1'
    else: bulbs[0][i-1]='0'
    return


N = int(input())
bulbs = []
cnt=0
for i in range(2):
    bulbs.append(list(input()))
for idx in range(N):
    if idx == 0:
        if bulbs[0][idx] != bulbs[1][idx] or bulbs[0][idx+1] != bulbs[1][idx+1]:
            change1(idx)
            cnt += 1
    elif idx==(N-1):
        if bulbs[0][idx] != bulbs[1][idx] and bulbs[0][idx - 1] != bulbs[1][idx - 1]:
            change2(idx)
            cnt += 1
            print(cnt)
        elif bulbs[0][idx] == bulbs[1][idx] and bulbs[0][idx - 1] == bulbs[1][idx - 1]:
            print(cnt)
        else :
            print(-1)
    else:
        if bulbs[0][idx-1] == bulbs[1][idx-1]:
            continue
        else:
            change(idx)
            cnt += 1