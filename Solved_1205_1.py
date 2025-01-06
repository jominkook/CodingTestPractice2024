N,S,P = map(int,input().split())



if N == 0 and S == 0 and P == 0:
    print(1)
    
else:
    rank = list(map(int,input().split()))
    if N >= P and rank[-1] >= S:
        print(-1)
    else:
        for i in range(N):
            if rank[i] <= S:
                print(i+1)
                break
        else:
            print(N+1)
            
# 1. N,S,P를 입력받는다.
