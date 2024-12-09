import sys
input = sys.stdin.readline

T = int(input())


for i in range(T):
    N = int(input())  
    stocks = list(map(int, input().split()))
    
    max_price = 0
    
    result = 0
    
    for j in range(N-1, -1, -1):
        if stocks[j] > max_price:
            max_price = stocks[j]
        else:
            result += max_price - stocks[j] 
            
            
            
    print(result)
    

    
    
    