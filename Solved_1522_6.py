#백준 1522

S = input().strip()
A = S.count('a')

S = S + S
min_A = float('inf')

for i in range(len(S)//2):
    window = S[i:i+A]
    min_A = min(min_A, window.count('a'))
    
print(min_A)
        