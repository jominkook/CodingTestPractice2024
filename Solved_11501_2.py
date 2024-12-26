#11501 주식

T = int(input())

for _ in range(T):
    N = int(input())
    
    stock = list(map(int, input().split()))
    
    max_price = stock[-1]
    
    result = 0
    
    for i in range(N - 2, -1, -1):
        if stock[i] < max_price:
            result += max_price - stock[i]
        else:
            max_price = stock[i]
            
    print(result)
    
    
    