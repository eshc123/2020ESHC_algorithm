import copy

def change(i,bulb):
    if bulb[0][i]=='0':
        bulb[0][i]='1'
    else: bulb[0][i]='0'
    if i!=0:
        if bulb[0][i-1]=='0':
            bulb[0][i-1]='1'
        else: bulb[0][i-1]='0'
    if i!=N-1:
        if bulb[0][i+1]=='0':
            bulb[0][i+1]='1'
        else: bulb[0][i+1]='0'
    return



N = int(input())
bulbs1 = [list(input()) for i in range(2)]
bulbs2 = copy.deepcopy(bulbs1)
cnt1=0
cnt2=0
c1,c2=False,False
for idx in range(N):
    if idx == 0:
        change(idx,bulbs1) # bulbs1 이 첫번째 바꾼거
        cnt1+=1
    elif idx==(N-1):
        if bulbs1[0][idx] != bulbs1[1][idx] and bulbs1[0][idx - 1] != bulbs1[1][idx - 1]:
            change(idx,bulbs1)
            cnt1 += 1
        elif bulbs1[0][idx] == bulbs1[1][idx] and bulbs1[0][idx - 1] == bulbs1[1][idx - 1]:
            pass
        else :
            c1=True
        if bulbs2[0][idx] != bulbs2[1][idx] and bulbs2[0][idx - 1] != bulbs2[1][idx - 1]:
            change(idx,bulbs2)
            cnt2 += 1
        elif bulbs2[0][idx] == bulbs2[1][idx] and bulbs2[0][idx - 1] == bulbs2[1][idx - 1]:
            pass
        else :
            c2=True

    else:
        if bulbs1[0][idx - 1] != bulbs1[1][idx - 1]:
            change(idx,bulbs1)
            cnt1 += 1
        if bulbs2[0][idx-1] != bulbs2[1][idx-1]:
            change(idx,bulbs2)
            cnt2 += 1
if c1 and c2:
    print(-1)
elif c1:
    print(cnt2)
elif c2:
    print(cnt1)
else:
    print(min(cnt1,cnt2))