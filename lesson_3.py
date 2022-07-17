def print_user_info(name, age, temp = 36.6, workspace = 'sportmaster'):
    print(f'User {name}, age {age}, temp {temp}, workspace {workspace}')

def check_user(name, age, temp):
    if age > 55 and temp > 37.0:
        print(f'User {name} should go to hosputal')
        return 'hospital'
    if age < 55 and temp > 37.0:
        print(f'User {name} should go to home')
        return 'home'
    else:
        print(f'User {name} should go to work')
        return 'work'

def daily_user_check(number_users):
    ill_users = []
    for _ in range(number_users):
        name, age, temp = input('Input name, age, temp: ').split()
        place = check_user(name, int(age), float(temp))
        if place != 'work':
            print(f'Ill person {name}')
            ill_users.append(name)
    return ill_users


#print(check_user('basil', 58, 38))
#check_user('Ivan', 20, 36)
#daily_user_check(2)
print_user_info('Katya', 22, temp=38)