x = int(input())
counter =0
if x >= 5:
    counter+= x//5
    x=x%5
if x >=4:
    counter+=x//4
    x=x%4
if x>=3:
    counter+=x//3
    x=x%3
if x>=2:
    counter+=x//2
    x=x%2
if x>=1:
    counter+=x//1
    x = x%2
print(counter)
