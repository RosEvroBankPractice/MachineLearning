from models import *
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


def work():
    user_grops_mas_dict = {}
    user_info_string = {}

    summary_info = ''

    for user in FacebookUser.select():
        join_groups = JoinGroups.filter(user=user)
        groups = []
        for join_group in join_groups:
            groups.append(join_group.group)
        user_grops_mas_dict[user.id] = groups

    for user_id in user_grops_mas_dict:

        info_string = ''
        for group in user_grops_mas_dict[user_id]:
            info_string += ' ' + group.name
        if (info_string != ''):
            print(user_id)
            user_info_string[user_id] = info_string
            summary_info += ' ' + info_string
            print(info_string)

    file = open('testfile5.txt', 'w')
    file.write(summary_info)
    file.close()

    my_phrases = []

    dict = {'клубы': 'клуб club fans', 'новости': 'интернет россия новости путин ссср',
            'юмор': 'юмор смех смеяться прикол анекдот',
            'бизнес': 'бизнес работа россия реклама заработок обьявление недвижимость бесплатный продажа продать',
            'жизнь': 'жизнь любовь дом здоровье ссср красота стиль',
            'путешествия': 'мир россия москва русский world путешествие отдых'}

    file = open('testfile4.txt', 'w')
    my_phrases = []
    file.write(str(dict) + '\n')
    i = 0

    # for key in dict:
    #    my_phrases.append(dict[key])
    #    file.write(str(i)+'   '+dict[key]+'\n')
    #    i+=1

    my_phrases.append(dict['новости'])
    my_phrases.append(dict['жизнь'])
    my_phrases.append(dict['бизнес'])


    user_mas=[]
    score_mas=[]
    for user_id in user_info_string:
        phrase = []
        phrase.append(user_info_string[user_id])
        vectorizer = TfidfVectorizer(min_df=1, stop_words='english')
        all_phrases = phrase + my_phrases
        my_features = vectorizer.fit_transform(all_phrases)
        scores = (my_features[0, :] * my_features[1:, :].T).A[0]

        print(str(user_id) + '   ' + str(scores))
        file.write(str(user_id) + '   ' + str(scores) + '\n')
        user_mas.append(user_id)
        score_mas.append(scores)
    file.close()

    return user_mas,score_mas
