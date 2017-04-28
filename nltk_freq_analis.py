import nltk

words = ['one', 'two', 'two', 'three', 'three', 'three']

print(words)
filttext = nltk.FreqDist(words)
for s in filttext:
    print(s)
    print(filttext[s])
