import sys
input = sys.stdin.readline


S = list(input().rstrip())

zero_cnt = S.count('0') // 2
one_cnt = S.count('1') // 2


answer = []

for s in S:
    if zero_cnt == 0 and one_cnt == 0:
        break
    
    if s == '0':
        if zero_cnt > 0:
            zero_cnt -= 1
            answer.append(s)
    else:
        if one_cnt > 0:
            one_cnt -= 1
            answer.append(s)
answer.sort()      
print(''.join(answer))

        
            







        
        

        
        

        

        
        