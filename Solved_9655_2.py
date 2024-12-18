#돌문제
import queue

N = int(input())

q = [0] * 1001
q[1] = 1

for i in range(2,1001):
    if q[i] == 0:
        if q[i-1] == 0 or q[i-3] == 0:
            q[i] = 1
        else:
            q[i] = 0
    else:
        q[i] = 0
        
if q[N] == 1:
    print("SK")  
else:
    print("CY")
    
    




