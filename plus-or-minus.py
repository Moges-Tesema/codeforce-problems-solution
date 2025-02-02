def plusOrMinus():
    a,b,c =list(map(int, input().split(" ")))
    if a+b==c:
        print("+")
    else:
        print("-")

test=int(input())
for i in range(test):
    plusOrMinus()