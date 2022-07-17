list_odd_num =[]
for i in range(0,50,2):
    list_odd_num.append(i * 5)
print(list_odd_num)

def num_sum(num):
    sum_of_digit = 0
    for char in str(num):
        sum_of_digit += int(char)
    return sum_of_digit

list_odd_num = (str(i * 5) + '!' for i in range(0, 50, 2) if num_sum(i * 5) % 2 == 0)
print(list_odd_num)

user_info = ['Basil', 'Ivanov', 27, 38, 45, 98]
user_info_num = (el for el in user_info if isinstance(el, int))
print(next(user_info_num))
print(next(user_info_num))
print(next(user_info_num))
print(next(user_info_num))

#print(user_info_num, type(user_info_num))

user_info = [['Basil', 'Ivanov'], ['Kirill', 'Petrov']]
user_info_more = ['bookshop', 'coffeeshop']

#new_user_info = [user.append(workplace) for user in user_info for workplace in user_info_more]
#print(new_user_info)

user_info_upper = [el.upper() for user in user_info for el in user]
print(user_info_upper)