# silver 3
# 영단어 암기는 괴로워

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
words = {}

for i in range(N):
    word = input().rstrip()
    l = len(word)
    
    if l >= M:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1

sorted_words = sorted(words.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for word in sorted_words:
    print(word[0])