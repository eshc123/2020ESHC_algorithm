import copy

def change_all(mtx,index):
    global coins1,cnt_min
    if index>=N:
        coins1 = [list(x) for x in zip(*coins1)]
        s = 0
        for i, coin in enumerate(coins1):
            n = cnt(coin)
            if N - n < n:
                coins1[i] = change(coins1, i)
                n = cnt(coin)
            s += n
        if cnt_min>s:
            cnt_min=s

        return
    else:
        change_all(mtx+[change(coins1,index)],index+1)
        change_all(mtx+[coins1[index]], index + 1)


def cnt(arr):
    c=0
    for i in arr:
        c+=i.count("T")
    return c


def change(a, indx):
    #print(indx,a[indx])
    arr=copy.deepcopy(a[indx])
    for i in range(len(arr)):
        if arr[i]=="T":
            arr[i]="H"
        else:
            arr[i]="T"
    return arr

def change1(arr):
    #print(indx,a[indx])
    #arr=copy.deepcopy(a[indx])
    for i in range(len(arr)):
        if arr[i]=="T":
            arr[i]="H"
        else:
            arr[i]="T"
    return arr


N = int(input())

coins1 = [list(input()) for i in range(N)]

cnt_min=400
for coin in coins1:
    n = cnt(coin)
    if N-n< n:
        coin=change1(coin)
print(coins1)

coins1 = [list(x) for x in zip(*coins1)]
s=0
for coin in coins1:
    n = cnt(coin)
    if N-n< n:
        coin=change1(coin)
        n = cnt(coin)
    s+=n
#change_all([],0)
print(s)
#
# for idx, coin in enumerate(coins1):
#     if coin.count("H")< coin.count("T"):
#         change(coin)
#
# cnt1 =cnt(coins1)
# print(coins1,coins2)
# for idx, coin in enumerate(coins2):
#     if coin.count("H")< coin.count("T"):
#         change(coin)
# cnt2 =cnt(coins2)
# coins3 = [list(x) for x in zip(*coins1)]
# for idx, coin in enumerate(coins3):
#     if coin.count("H")< coin.count("T"):
#         change(coin)
# cnt3 =cnt(coins3)
# coins4 = [list(x) for x in zip(*coins2)]
# for idx, coin in enumerate(coins4):
#     if coin.count("H")< coin.count("T"):
#         change(coin)
# cnt4 =cnt(coins4)
# print(min(cnt1,cnt2),cnt1,cnt2)