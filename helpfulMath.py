nums=list(map(int,input().split("+")))
nums.sort()
ans=str(nums[0])
for i in range(1,len(nums)):
    ans+="+"+str(nums[i])
print(ans)