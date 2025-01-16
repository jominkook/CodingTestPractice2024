#백준 크로스 컨트리


T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x: x[0])
    max_val = 0
    for i in range(N):
        for j in range(i+1, N):
            if arr[i][1] > arr[j][1]:
                max_val = max(max_val, arr[i][0] - arr[j][0] + arr[i][1] - arr[j][1])
    print(max_val)

    

    



    