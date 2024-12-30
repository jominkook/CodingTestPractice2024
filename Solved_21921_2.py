N,X = map(int, input().split())

visited_people = list(map(int, input().split()))

sum_people = sum(visited_people[:X])

max_sum = sum_people

count = 1
if max_sum == 0:
    print("SAD")
    exit()
    
for i in range(X,N):
    sum_people = sum_people - visited_people[i-X] + visited_people[i]
    if sum_people > max_sum:
        max_sum = sum_people
        count = 1
    elif sum_people == max_sum:
        count += 1
        
print(max_sum)
print(count)




