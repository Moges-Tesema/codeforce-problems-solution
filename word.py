upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
word = input()
upperCounter=0
lowerCounter=0
for i in word:
    if i in upper:
        upperCounter+=1
    else:
        lowerCounter+=1
if upperCounter > lowerCounter:
    print(word.upper())
else:
    print(word.lower())