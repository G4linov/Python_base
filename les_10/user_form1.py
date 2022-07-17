from Lesson_10 import BirthForm, WorkExchange, Taxes, Workplaces

user_0_birth_form = BirthForm(name='Basil', surname='Ivanov',
                              mothers_name="Nata", fathers_name="Dima", birth_date=1994, )
user_0 = WorkExchange(birth_form=user_0_birth_form, worplaces=None, new_workplace=None)

print("Compare result", WorkExchange.compare_info_from_both(user_0_birth_form, user_0))

user_0_taxes = Taxes()
print(user_0_taxes.annual_taxes)
user_0_taxes.annual_taxes = 0.1
print("Print", user_0_taxes._annual_taxes)
user_0_taxes.annual_taxes = 0.1
print(user_0_taxes.annual_taxes)
print(user_0_taxes.percent)
# print(user_0_taxes + 5000)
# user_0_taxes + 10
# print(user_0_taxes.annual_taxes)
# print(user_0_taxes > user_0_salary)

workplaces = Workplaces(['coffee', 'bookshop', 'zara'])

for w in workplaces:
    print(w)
# print(next(workplaces))
# print(next(workplaces))
# print(next(workplaces))
# print(next(workplaces))
# print(next(workplaces))
# print(next(workplaces))



