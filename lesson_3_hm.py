import random as rd


'''
Написать функцию num_translate(), переводящую числительные
от 0 до 10 c английского на русский язык. Например:

>>> >>> num_translate("one")
"один"
>>> num_translate("eight")
"восемь"

Если перевод сделать невозможно, вернуть None.
Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
'''

from ast import arg

from pip import main


def num_translate(main_dict, key):
    if main_dict.get(key):
        print(main_dict[key])
    else:
        return None

main_dict = {'one': 'один',
             'two': 'два',
             'three': 'три',
             'four': 'четыре',
             'five': 'пять',
             'six': 'шесть',
             'seven': 'семь',
             'eight': 'восемь',
             'nine': 'девять',
             'ten': 'десять'}

num_translate(main_dict, 'five')

'''
 Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
 в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:

>>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"], 
    "М": ["Мария"], "П": ["Петр"]
}

Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?
'''

def thesaurus(*args):
    main_dict_names = {}

    for key in args:
        if main_dict_names.get(key[0]) == None:
            main_dict_names[key[0]] = []
            main_dict_names[key[0]].append(key)
        else:
            main_dict_names[key[0]].append(key)

    for keey, value in main_dict_names.items():
        print("{0}: {1}".format(keey,value))

thesaurus("Иван", "Мария", "Петр", "Илья")

'''
Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в 
котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия
 начинается с соответствующей буквы. Например:

>>> >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": "Петр Алексеев"
    }, 
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"], 
        "А": ["Анна Савельева"]
    }
}

Сможете ли вы вернуть отсортированный по ключам словарь?
'''

def thesaurus_adv(*args):
    main_dict_names = {}

    for key in args:
        if main_dict_names.get(key.split()[1][0]) == None:
            main_dict_names[key.split()[1][0]] = {}
            if (main_dict_names[key.split()[1][0]]).get(key.split()[0][0]) == None:
                (main_dict_names[key.split()[1][0]])[key.split()[0][0]] = []
                (main_dict_names[key.split()[1][0]])[key.split()[0][0]].append(key)
            else:
                (main_dict_names[key.split()[1][0]])[key.split()[0][0]].append(key)
        else:
            if (main_dict_names[key.split()[1][0]]).get(key.split()[0][0]) == None:
                (main_dict_names[key.split()[1][0]])[key.split()[0][0]] = []
                (main_dict_names[key.split()[1][0]])[key.split()[0][0]].append(key)
            else:
                (main_dict_names[key.split()[1][0]])[key.split()[0][0]].append(key)

    for keey, value in main_dict_names.items():
        print("{0}: {1}".format(keey,value))

thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков:
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

        Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
'''

def get_jokes(num):

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    joke_list = []

    for _ in range(num):
        joke = ''
        joke += nouns[rd.randint(0, len(nouns)-1)]
        joke += ' ' + adverbs[rd.randint(0, len(adverbs)-1)]
        joke += ' ' + adjectives[rd.randint(0, len(adjectives)-1)]
        joke_list.append(joke)
    
    print(joke_list)

get_jokes(7)