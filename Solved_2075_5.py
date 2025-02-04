from collections import deque
#백준 2075 N번째 큰수
#5번째 풀이

N = int(input())

#시간초과 ㅠㅠ
# num_list = []

# for i in range(N):
#     num_list.append(list(map(int, input().split())))
    
# num_list.sort(reverse=True)

# print(num_list[N-1])
queue = deque()

for i in range(N):
    queue.extend(list(map(int, input().split())))
    queue = deque(sorted(queue, reverse=True)[:N])
    
print(queue[-1])

