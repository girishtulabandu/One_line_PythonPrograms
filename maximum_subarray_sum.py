#nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation : [4,-1,2,1]
r = max([sum(nums[i:i+j]) for i in range(0,len(nums)) for j in range(1,len(nums)-i+1)])
