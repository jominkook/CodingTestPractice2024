N,M = map(int,input().split())

queue = [i for i in range(1,N+1)]

arr = list(map(int,input().split()))

cnt = 0


def bfs():
    global cnt
    while arr:
        if queue[0] == arr[0]:
            queue.pop(0)
            arr.pop(0)
        else:
            if queue.index(arr[0]) <= len(queue)//2:
                while queue[0] != arr[0]:
                    queue.append(queue.pop(0))
                    cnt += 1
            else:
                while queue[0] != arr[0]:
                    queue.insert(0,queue.pop())
                    cnt += 1
bfs()
print(cnt)