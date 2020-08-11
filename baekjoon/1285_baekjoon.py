N = int(input())
coins = [list(input()) for i in range(N)]
cnt_h,cnt_t= 0,0
max_t,index = 0,0
for idx, coin in enumerate(coins):
    if max_t< coin.count("T"):
        max_t = coin.count("T")
        index = idx
    cnt_h += coin.count("H")
    cnt_t += coin.count("T")
print(cnt_t-max_t+(N-max_t))
