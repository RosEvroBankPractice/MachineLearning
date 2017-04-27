import nltk
import string

from collections import Counter

def get_tokens():

    text = """

    Любой data scientist ежедневно работает с большими объемами данных. Считается, что около 60% – 70% времени занимает первый этап рабочего процесса: очистка, фильтрация и преобразование данных в формат, подходящий для применения алгоритмов машинного обучения. На втором этапе выполняется предобработка и непосредственное обучение моделей. В сегодняшней статье мы сконцентрируемся на втором этапе процесса и рассмотрим различные техники и рекомендации, являющиеся результатом моего участия более чем в 100 соревнованиях по машинному обучению. Несмотря на то, что описанные концепции имеют достаточно общий характер, они будут полезны при решении многих конкретных задач.

Все примеры кода написаны на Python!


    """
    lowers = text.lower()
    #remove the punctuation using the character deletion step of translate
    no_punctuation = lowers.translate()
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

tokens = get_tokens()
count = Counter(tokens)
print (count.most_common(10))