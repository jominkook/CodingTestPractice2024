#백준 11501번 주식
# 3번째 풀이과정
T = int(input())

for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    max_price = 0
    profit = 0
    
    #마지막날부터 첫날금액을 비교하여 
    # 비교한 날보다 더 큰 금액이면 그 차이만큼 이익을 더해준다.
    # 비교한 날보다 더 작은 금액이면  비교한 날 금액을 최대금액으로 설정한다.
    for i in range(N-1, -1, -1):
        if stock[i] > max_price:
            max_price = stock[i]
        else:
            profit += max_price - stock[i]
                  
    print(profit)
    