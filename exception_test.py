from logging import exception


dif_chars = ['10', '0', 'o', 10.1]
for c in dif_chars:
    try:
        x = print(10/int(c))
    except ValueError:
        print('This line is skipped')
        x = None
    except ZeroDivisionError:
        print('It was zero!', 10)
        x = 10
    finally:
        print('Tha\'s all')
        x = 0

print('Hello!', x)

class TooYoung(Exception):
    def __init__(self, age):
        self.message = f'Too short for this park. Come after {10-age}'
        super().__init__(self.message)

def age_check(age):
    if age < 10:
        raise TooYoung(age)
    else:
        print(age)

age_list = [11, 7, '12', 13, 18, 9, 8]

for age in age_list:
    try:
        age_check(age)
    except TooYoung:
        print('It\'s ok')
    except TypeError:
        print('Was cleand')
        age_check(int(age))