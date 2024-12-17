import sys
sys.stdin.readline

N = int(input())

stones = [0] * 1001

stones[1] = 1

for i in range(2, 1001):
    if stones[i-1] == 0 or stones[i-3] == 0:
        stones[i] = 1
    elif stones[i-1] == 1 and stones[i-3] == 1:
        stones[i] = 0
        
if stones[N] == 1:
    print("SK")
else:
    print("CY")

