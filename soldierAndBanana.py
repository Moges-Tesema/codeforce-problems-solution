firstCost, dollar,bananas = list(map(int,input().split()))
cost=0
for i in range(1,bananas+1):
    cost+= i*firstCost
if dollar >= cost:
    print(0)
else:
    print(cost-dollar)
