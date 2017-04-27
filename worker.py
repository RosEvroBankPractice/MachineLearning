from models import *
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np



user_grops_mas_dict={}
user_info_string={}

summary_info=''

for user in FacebookUser.select():
    join_groups = JoinGroups.filter(user=user)
    groups=[]
    for join_group in join_groups:
        groups.append(join_group.group)
    user_grops_mas_dict[user.id]=groups

for user_id in user_grops_mas_dict:

    info_string=''
    for group in user_grops_mas_dict[user_id]:
        info_string+=' '+group.name
    if(info_string!=''):
        print(user_id)
        user_info_string[user_id]=info_string
        summary_info+=' '+info_string
        print(info_string)

file = open('testfile.txt', 'w')
file.write(summary_info)
file.close()





my_phrases = ["мир русский новость путин ссср russian ",
              "бизнес",
              "юмор анекдоты смех"]



file = open('testfile4.txt', 'w')

for user_id in user_info_string:
    phrase = []
    phrase.append(user_info_string[user_id])
    vectorizer = TfidfVectorizer(min_df=1, stop_words='english')
    all_phrases = phrase + my_phrases
    my_features = vectorizer.fit_transform(all_phrases)
    scores = (my_features[0, :] * my_features[1:, :].T).A[0]

    print(str(user_id)+'   '+str(scores))
    file.write(str(user_id)+'   '+str(scores)+'\n')
file.close()

