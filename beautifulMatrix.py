
arr=[]
x=0
y=0
for i in range(5):
    arr.append(list(map(int, input().split(" "))))
for i in range(5):
    for j in range(5):
        if arr[i][j] !=0:
            x=i+1
            y=j+1
            break
    if x:
        break
print(abs(x-3)+abs(y-3))