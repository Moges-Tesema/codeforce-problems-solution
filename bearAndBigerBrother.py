a,b=list(map(int,input().split()))
year=0
while(b>=a):
    year+=1
    b*=2
    a*=3
print(year)