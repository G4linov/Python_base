'''
bool float isidigit range
list (списки)
'''

list_of_animals = ['cats', 'dogs', 'cows']
list_of_animals_saved = list_of_animals.copy()
#print(list_of_animals.pop(1))
#print(list_of_animals)
#print(list_of_animals[2])
#print(list_of_animals[-1])
#print(list_of_animals[-3])
list_of_animals[-1] = 'rats'

test_string = 'На марсе будут яблони цвести'
mars_list = list(test_string)
print(mars_list[:9])
print(mars_list[3:9])
print(mars_list[3:15:3])
print(mars_list[::3])
print(mars_list[::-1])
print(mars_list[9:0:-1])
print(mars_list[:50])

space_ships = ['Буран', 'Шаттл дисковери']
mars_list.append(space_ships)
print(mars_list)
print(mars_list[-1][-1])
mars_list.append('Sputnik')
print(mars_list)
mars_list.extend(list('potato'))
print(mars_list)

#############
cosmo_bag = []
for i in range(5):
    cosmo_bag.extend(mars_list[i])
print(cosmo_bag)
##############

space_ships.insert(1,'Challanger')
space_ships.insert(3,'Challanger')
print(space_ships)
print(space_ships.index('Шаттл дисковери'))

num_list_1 = [1, 2, 3, 4, 5, 6]
num_list_2 = [1, 2, 3, 4, 5, 6]
print(num_list_1 + num_list_2)

print(dir(num_list_2))
print(space_ships.count('Challanger'))

'''
Посчитать кол-во символов с во всем списке sapce_ships
'''
space_ships.remove('Challanger')
space_ships.reverse()
space_ships.append('Коламбия')
#space_ships.sort() #По месту, меняет сам объект
space_ships = sorted(space_ships, reverse=True) #возвращает нвоый объект
print(space_ships)

space_men = ('Гагарин', 'Армстронг', 'Леонов')
print(type(space_men), type(space_ships))
#space_men[0] = 'Титов' - кортежи неизменяемы
print(dir(space_men))