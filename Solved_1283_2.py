import sys

input = sys.stdin.readline

N = int(input())

keys = []


for i in range(N):
    words = input().split()
    
    for j in range(len(words)):
        if words[j] not in keys:
            words[j] = words[j].upper()
            keys.append(words[j])
            
print(keys)
        
    
        
        
        
    