s = input()

a = s.count('a')    
s = s + s

min_val = float('inf')

for i in range(len(s)//2):
    min_val = min(min_val, a - s[i:i+a].count('a'))
    
print(min_val)
        
        

