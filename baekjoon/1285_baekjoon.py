def cnt(arr):
    c=0
    for i in arr:
        c+=i.count("T")
    return c

def change(arr):
    for i in range(len(arr)):
        if arr[i]=="T":
            arr[i]="H"
        else:
            arr[i]="T"


N = int(input())
coins1 = [list(input()) for i in range(N)]
coins2 = [list(x) for x in zip(*coins1)]
cnt1,cnt2,cnt3=0,0,0

for idx, coin in enumerate(coins1):
    if coin.count("H")<= coin.count("T"):
        change(coin)

cnt1 =cnt(coins1)
for idx, coin in enumerate(coins2):
    if coin.count("H")<= coin.count("T"):
        change(coin)
cnt2 =cnt(coins2)
coins3 = [list(x) for x in zip(*coins1)]
for idx, coin in enumerate(coins3):
    if coin.count("H")<= coin.count("T"):
        change(coin)
cnt3 =cnt(coins3)
coins4 = [list(x) for x in zip(*coins2)]
for idx, coin in enumerate(coins4):
    if coin.count("H")<= coin.count("T"):
        change(coin)
cnt4 =cnt(coins4)
print(min(cnt1,cnt2,cnt3,cnt4),cnt1,cnt2,cnt3,cnt4)