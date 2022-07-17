def print_user_info_list(*args, name ="katya"):
    print(f"User {name}, {' '.join(list(map(str, args)))}")

def print_user_info(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append(f'{str(key)} : {value} ')
    print(f"User {''.join(result)}")


user_info_list = ['Basil', 'Ivanov', 27, 36.6, True]
print_user_info_list(*user_info_list)

user_info_dict = {'name': 'Basil',
                  'age': 27,
                  'workspace': 'starbucs',
                  'temp': 36.6,
                  'was_ill': True}

print_user_info(**user_info_dict)

print(user_info_dict.keys())
all_test_keys = list(user_info_dict.keys())
all_test_keys.extend(['working hours', 'holidays'])
for key in all_test_keys:
    print(key, user_info_dict.get(key, 'Sorry, no key'))

user_old_work_info = {'recommendation': 'good', 'First work': True}
user_info_dict['temp'] = 38.1
print(user_info_dict)
user_info_dict.update(user_old_work_info)
print(user_info_dict)
user_info_dict['file_10'] = 42
print(user_info_dict)
del user_info_dict['file_10']
print(user_info_dict)

#print(user_info_dict.get('working hours', [9, 18]))

def check_is_ill(user_info):
    if user_info.get('temp') == None:
        print('Check temp!')
        return True
    if user_info.get('temp') > 37.0:
        return True
    else:
        return False

all_users = [{'name': 'Basil', 'temp': 36.6},
             {'name': 'Katya', 'temp': 38.6}]

ill_users = filter(lambda x: x.get('temp') > 37.0, all_users)
print(*ill_users)