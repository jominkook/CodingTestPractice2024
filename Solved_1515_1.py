import sys


nums = list(input())

i = 0

while True:
    i = i+1
    num = list(str(i))
    
    while len(num)> 0 and len(nums) > 0:
        if num[0] == nums[0]:
            num.pop(0)
            nums.pop(0)
        else:
            num.pop(0)
            
    if len(nums) == 0:
        break
    
print(i)
    
       