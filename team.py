prob=int(input())
imp=0
for i in range(prob):
    friends=list(map(int,input().split(" ")))
    if friends.count(1)>=2:
        imp+=1
print(imp)
