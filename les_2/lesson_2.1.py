from tokenize import Ignore
from xml.dom.minidom import Element


cosmo_str = 'на Марсе будут яблони цвести'
print(cosmo_str[0])
#cosmo_str[0] = 'Н' #Строки как кортеж
cosmo_str += '!'
print(cosmo_str)

potato_list = list('potato')
print(potato_list)
print(''.join(potato_list))
new_potato = ''.join(potato_list)

dirs_path = ['root', 'home', 'funny_picturres']
path = '/'.join(dirs_path)
path_split = path.split('/')
print(path_split)

print(cosmo_str.capitalize())
cosmo_words = cosmo_str.split()
print(dir(cosmo_str))
#print(cosmo_words)
#print(cosmo_str.center(1,'Q'))
#str_enc = cosmo_str.encode()
#print(str_enc.decode())

test_emails = ['777@gmAil.com', 'asdasd@gmail.ru', 'Grat@gmaiL.com']
#print(cosmo_str.endswith('!'))

results = [el.lower().endswith('@gmail.com') for el in test_emails]
'''
result = []
for el in test_emails:
    result.append(el.endswith('@gmail.com'))
'''
print(results)
print('KATYA'.lower())

print(ord('A'), ord('a')) #32 points

lower_test = "Шел медвЕдь По Лесу. See CAR is BuRniNg."
new_str = []
for el in lower_test:
    if el.isupper():
        new_str.append(chr((ord(el) + 32)))
    elif el == ' ' or el == '.':
        new_str.append(el)
    else:
        new_str.append(chr((ord(el) - 32)))

print(''.join(new_str))

print(ord('а'),ord('А'))
print(ord('я'),ord('Я'))
print(ord('a'),ord('A'))
print(ord('z'),ord('Z'))

print(lower_test.replace('CAR', 'bmw'))