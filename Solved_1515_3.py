#백준 1515 수 이어 쓰기 
# 3번째 풀이
num = list(str(input()))
i = 0

while True:
    
    i = i + 1
    nums = list(str(i))
    
    while len(num) > 0 and len(nums) > 0:
        if num[0] == nums[0]:
            num.pop(0)
            nums.pop(0)
        else:
            nums.pop(0)
            
    if len(num) == 0:
        break
    
print(i)
            
    
    