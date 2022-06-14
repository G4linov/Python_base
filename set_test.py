name_list = ['Basil', 'Kirill', 'Basil', 'Kate', 'Kate', 'Kate', 'Kate', 'Lena']
print(name_list)

name_set = set(name_list)
print(name_set)

#print(dir(name_set))
name_set.add('Lena')
name_set.add('Ivan')

girls_name = {'Lena', 'Kate'}
girls_name_other = {'Lena', 'Kate', 'Sasha', 'Olya'}

print(name_set.intersection(girls_name_other))
print(name_set.intersection(girls_name))

print(name_set.difference(girls_name_other))
print(name_set.difference(girls_name))

print(name_set.issubset(girls_name))
print(girls_name.issubset(name_set))
print(name_set.issubset(girls_name_other))