import nltk
import string
from nltk.corpus import stopwords
import re
import string
import pymorphy2
import operator

def tokenize_me(file_text):
    #firstly let's apply nltk tokenization
    tokens = nltk.word_tokenize(file_text)

    #let's delete punctuation symbols
    tokens = [i for i in tokens if ( i not in string.punctuation )]

    #deleting stop_words
    stop_words = stopwords.words('russian')
    stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на',"''","``"])
    stop_words.extend(stopwords.words('english'))
    tokens = [i for i in tokens if ( i not in stop_words )]

    #cleaning words
    tokens = [i.replace("«", "").replace("»", "") for i in tokens]

    return tokens



file = open('testfile.txt', 'r')
text=file.read()
#print(text)


tokens=tokenize_me(text)


morph = pymorphy2.MorphAnalyzer()
result_set=set()
result_list=[]
for part in tokens:
    m = morph.parse(part)
    if m:
        word = m[0]
        if word.tag.POS not in ("NUMR", "PREP", "CONJ", "PRCL", "INTJ"):
            result_set.add(word.normal_form)
            result_list.append(word.normal_form)


print(result_set)
print(result_list)


freq_dist=nltk.FreqDist(result_list)
freq_dict={}
for s in freq_dist:
    #print(s)
    #print(freq_dist[s])
    freq_dict[s]=freq_dist[s]

sorted_freq_tuple=sorted(freq_dict.items(),key=operator.itemgetter(1))
print(sorted_freq_tuple)
reversed_sorted_freq_tuple=list(reversed(sorted_freq_tuple))
print(reversed_sorted_freq_tuple)

file = open('testfile2.txt', 'w')

for tuple in reversed_sorted_freq_tuple:
    file.write(str(tuple[0])+ ', '+str(tuple[1])+'\n')
    print(tuple)

file.close()








