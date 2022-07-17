from abc import ABC, abstractmethod

"""
МФЦ:
* заполняет форму в зависимости от своего запроса
* свидетельство о рождении
* смена рабочего места
* заявка на загран паспорт
* держим у уме что нам нужно что-то еще будет добавить

* создание данной формы (пользователь ее заполнил)
* редактирование
* подтягивание информации из другой формы
"""


class BaseCommunication(ABC):
    @abstractmethod
    def communication_with_taxes(self):
        pass

    @abstractmethod
    def communication_with_salary(self):
        pass

    @abstractmethod
    def communication_with_birthform(self):
        pass

    @abstractmethod
    def communication_with_pfr(self):
        pass


class BaseForm:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @staticmethod
    def compare_info_from_both(form_1, form_2):
        return form_1.__dict__.items() == form_2.__dict__.items()

    def __str__(self):
        result = [f'{key} : {value}' for key, value in self.__dict__.items()]
        return ', '.join(result)

    # def __del__(self):
    #     print(f'Form were removed! {type(self)}')


class BirthForm(BaseForm, BaseCommunication):
    attr_set = frozenset(['name', 'surname',
                          'mothers_name', 'fathers_name', 'birth_date'])

    def check_for_correctness(self):
        if BirthForm.attr_set.issubset(set(self.__dict__.keys())):
            return True
        else:
            return False

    def communication_with_birthform(self):
        pass

    def communication_with_taxes(self):
        pass

    def communication_with_salary(self):
        pass

    def communication_with_pfr(self):
        # self.__get_info_from_birthdate()
        print(f'Data of {str(self)} were send to PFR')


class WorkPlace:
    def __init__(self, workplace_name):
        self.workplace_name = workplace_name

    def __str__(self):
        return self.workplace_name


class Workplaces:
    def __init__(self, workplaces):
        self.workplaces = list(map(WorkPlace, workplaces))
        self.i = len(workplaces)
        self.length = len(workplaces) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > 0:
            self.i -= 1
            return self.workplaces[self.i]
        else:
            raise StopIteration


class WorkExchange(BaseForm, BaseCommunication):
    attr_set = frozenset(['birth_form',
                          'workplaces', 'new_workplaces'])

    def check_for_correctness(self):
        if WorkExchange.attr_set.issubset(set(self.__dict__.keys())):
            return True
        else:
            return False

    def communication_with_birthform(self):
        """
        обновить атрибуты объекта класса, получив их из свидетельства о рождении
        """
        for key, value in self.birth_form.__dict__:
            if key in {'name', 'surname', 'birth_date'}:
                self.__dict__[key] = value

        # pass

    def communication_with_pfr(self):
        # self.__get_info_from_birthdate()
        print(f'Data of {str(self)} were send to PFR')

    def communication_with_taxes(self):
        pass

    def communication_with_salary(self):
        pass


class Salary:
    def __init__(self, salary):
        self.current_salary = salary


class Taxes:
    def __init__(self):
        self._annual_taxes = 100
        self.threshold = 500
        self.__percent = 0

    @property
    def annual_taxes(self):
        return self._annual_taxes

    @annual_taxes.setter
    def annual_taxes(self, percent):
        self.__percent += percent
        self._annual_taxes = self.annual_taxes * (1 + self.__percent)

    @property
    def percent(self):
        return self.__percent

    def __gt__(self, other):
        return other.current_salary > self.threshold


class WorkBook(BaseForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.salary = Salary(kwargs['salary'])
        self.taxes = Taxes()
