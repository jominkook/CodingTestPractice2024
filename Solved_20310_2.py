#백준 20310 
#2번째 풀이

S = list(input())

zero = S.count('0') // 2
one = S.count('1') // 2

for i in range(zero):
    S.pop(-S[::-1].index('0')-1)
for i in range(one):
    S.pop(S.index('1'))
    
print(''.join(S))
        
        