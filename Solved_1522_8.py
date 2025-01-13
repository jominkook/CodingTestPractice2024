T = int(input())

for i in range(T):
    N = int(input())
    
    stock = list(map(int, input().split()))
    
    max_price = stock[-1]
    
    profit = 0
    
    for j in range(N-2, -1, -1):
        if stock[j] < max_price:
            profit += max_price - stock[j]
        else:
            max_price = stock[j]
            
    print(profit)
    
        
    
    
            
        
    