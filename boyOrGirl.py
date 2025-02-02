username = input()
newUsername=""
for i in range(len(username)):
    if username[i] not in newUsername:
        newUsername+=username[i]
if len(newUsername)%2==0:
    print("CHAT WITH HER!")
else:
    print( "IGNORE HIM!")