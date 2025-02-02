n, k = list(map(int,input().split()))
points = list(map(int,input().split()))
k = points[k-1]
adviced =0
for i in range(n):
    if points[i] >= k and points[i]>0:
        adviced+=1
    else:
        break
print( adviced)