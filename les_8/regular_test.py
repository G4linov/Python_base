import re

random_words = ['words', 'василий', 'Кирилл', 'Кирилл7', 'Ваа каа', 'кКир', 'Кирилл77', 'Кирилл 1117', 'Василий56', 'Василий 565']

# \d - абсолютно любая одна цифра
# \s - пробельный символ
# \w - любой символ
# . - один символ кроме переноси строки
#pattern = re.compile(r'^[А-ЯЁ][а-яё]+\d$|^[А-ЯЁ][а-яё]+$')
#pattern = re.compile(r'Кир')
pattern = re.compile(r'[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+')

#for word in random_words:
#    print(pattern.match(word))
#    if pattern.search(word):
#        coords = pattern.search(word).span()
#        print(word[coords[1]:])

forum_message = 'Василий Иванов под ником p@nisher96 писал оскорбления' \
                ' на почту sunny_girl@yandex.ru 21/08/2020' \
                ' и hello_kitty_2000@gmail.com 23.08.2020'

larisa_yuriy = re.compile(r'\w+@\w+[.]\w+')
tihiy_larisa = re.compile(r'(?:\d{2}[./|]){2}\d{4}')
paverl = re.compile(r'\w+@\w+')
#print(paverl.split(forum_message))
print(larisa_yuriy.findall(forum_message))
print(tihiy_larisa.findall(forum_message))