def find_22(nums):
    for i in range(0,len(nums)-1):
        if(nums[i]==2 and nums[i+1]==2):
            return True
    return False

print(find_22([1,2,2,3])) # False
print(find_22([1,2,3,2,4])) # True
