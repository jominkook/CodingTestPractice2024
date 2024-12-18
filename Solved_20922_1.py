#풀이1

import sys
sys.stdin.readline

N,K = map(int,input().split())

sequence = list(map(int,input().split()))

def find_max_length(sequence):
    max_length = 0
    length = 0
    count = {}
    start = 0
    end = 0
    while end < N:
        if sequence[end] in count:
            count[sequence[end]] += 1
        else:
            count[sequence[end]] = 1
        length += 1
        if count[sequence[end]] > K:
            while count[sequence[end]] > K:
                count[sequence[start]] -= 1
                length -= 1
                start += 1
        max_length = max(max_length,length)
        end += 1
    return max_length

print(find_max_length(sequence))



