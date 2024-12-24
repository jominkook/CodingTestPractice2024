
import sys

N, K = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0

num_dict = {}
max_length = 0

while right < N:
    if num_list[right] in num_dict:
        num_dict[num_list[right]] += 1
    else:
        num_dict[num_list[right]] = 1

    while num_dict[num_list[right]] > K:
        num_dict[num_list[left]] -= 1
        if num_dict[num_list[left]] == 0:
            del num_dict[num_list[left]]
        left += 1

    max_length = max(max_length, right - left + 1)
    right += 1

print(max_length)