# 백준 1515 수 이어 쓰기
# 2차 시도: 성공

import sys
input = sys.stdin.readline

nums = str(input().rstrip())

i = 0

while True:
    i = i+1
    num = str(i)
    
    while len(num)> 0 and len(nums) > 0:
        if num[0] == nums[0]:
            num = num[1:]
            nums = nums[1:]
        else:
            num = num[1:]
            
    if len(nums) == 0:
        break
    
print(i)      
            
    

