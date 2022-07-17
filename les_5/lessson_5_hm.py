'''
EX1

 Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...

'''


def odd_num(n):
    for i in range(1, n+1, 2):
        yield i

odd_to_15 = odd_num(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))

print('##############')

#n = int(input())+1
n = 16
gen_odd_num = (i for i in range(1, n, 2))

for el in gen_odd_num:
   print(el)

print('##############')

'''
 Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
'''
from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

#gen_tutor_klass = ((user,el) for user in tutors for el in klasses)

#for _ in range(len(tutors)):
#    print(next(gen_tutor_klass))

rez = zip_longest(tutors, klasses[:len(tutors)], fillvalue=None)
print(list(rez))

print('##############')

'''
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
'''

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [src[n+1] for n in range(len(src)-1) if src[n] < src[n+1]]
print(result)

print('##############')

'''

'''