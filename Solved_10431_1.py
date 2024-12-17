P = int(input())

for _ in range(P):
    T, *heights = map(int, input().split())
    childheight = heights[:20]
    count = 0
    
    for i in range(20):
        for j in range(19, i, -1):
            if childheight[j] < childheight[j-1]:
                childheight[j], childheight[j-1] = childheight[j-1], childheight[j]
                count += 1
                
    print(T, count)