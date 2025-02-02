n=int(input())
x=0
for i in range(n):
    stm=input()
    if '+' in stm:
        x+=1
    else:
        x-=1
print(x)
