T = int(input())
color_costs = []
for i in range(T):
    color_costs.append(list(map(int,input().split())))
d = color_costs.copy()
for i in range(0,T-1):
        d[i+1][0]=min(color_costs[i][1],color_costs[i][2])+d[i+1][0]
        d[i+1][1]=min(color_costs[i][0],color_costs[i][2])+d[i+1][1]
        d[i+1][2]=min(color_costs[i][1],color_costs[i][0])+d[i+1][2]
print(min(d[T-1]))