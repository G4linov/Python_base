'''
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
'''

from re import L
import time

class TrafficLight:
    def __init__(self):
        self.__color = None
        self.running = False

    def color(self):
        colors = ['Red', 'Yellow', 'Green']
        if self.running == False:
            return print('U should turn on Traffic Light')
        else:
            while self.running == True:
                counter = 0
                for key in colors:
                    self.__color = key
                    print(self.__color)
                    if counter == 0:
                        time.sleep(7)
                    elif counter == 1:
                        time.sleep(2)
                    else:
                        time.sleep(4)
                test = input('For turn off Traffic Light write \'0\' for continue \'1\'')
                if int(test) == 0:
                    self.running = False

    def turn(self, tumbler:bool):
        if tumbler == True:
            self.running = True
            return print('Traffic Light on')
        else:
            self.running = False
            return print('Traffic Light off')

#Mira_TrafficLight = TrafficLight()
#Mira_TrafficLight.color()
#Mira_TrafficLight.turn(1)
#Mira_TrafficLight.color()

'''
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''

class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def massa(self):
        return print(self._lenght * self._width * 25 * 0.05, 't')

#Mira_Road = Road(5000, 20)
#Mira_Road.massa()

'''
Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income

class Position(Worker):
    def get_full_name(self):
        for key, value in self.

    def get_total_income(self):
        pass