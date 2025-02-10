# 백준 1157 단어공부
# 1번째 풀이

import sys
input = sys.stdin.readline

word = input().strip().upper()

word_dict = {}
for i in word:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1
        
max_value = max(word_dict.values())
max_key = [k for k, v in word_dict.items() if v == max_value]

if len(max_key) > 1:
    print('?')
    
else:
    print(max_key[0])


    