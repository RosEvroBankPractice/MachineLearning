import re
import string
import pymorphy2

data = """
кот коту кота коты кошек кошкам котам
собака собаки собаке собакам
""".lstrip()

# иду гулять сегодня
#а еще сегодня а б в и тогда гулять гулять гулять

#Требования: Владение пакетом прикладных программ MS Office (MS Excel‚ PowerPoint); Требуется опыт подготовки презентаций (!).
#Обязанности: проверки целевого и эффективного расходования средств бюджета; опыт работы аналитиком, экономистом от 2 лет; отличное знание Excel; знание техник и методик анализа;


PUNCTUATION = re.compile("[\\d\\{}]".format("\\".join(string.punctuation)))

morph = pymorphy2.MorphAnalyzer()
result = set()

for line in data.splitlines():
    line = PUNCTUATION.sub("", line).split()
    for part in line:
        m = morph.parse(part)
        if m:
            word = m[0]
            if word.tag.POS not in ("NUMR", "PREP", "CONJ", "PRCL", "INTJ"):
                result.add(word.normal_form)

print(result)