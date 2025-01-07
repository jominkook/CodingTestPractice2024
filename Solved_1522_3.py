S = input()
A = S.count('a')

S += S[0:A-1]
min_val = float('inf')
for i in range(len(S)-(A-1)):
    min_val = min(min_val,S[i:i+A].count('b'))
    
print(min_val)