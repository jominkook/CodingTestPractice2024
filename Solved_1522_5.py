S = str(input())

A = S.count('a')

for i in range(len(S) - (A-1)):
    if S[i:i+A] == 'a'*A:
        print(A)
        exit()
        
print(0)
   
